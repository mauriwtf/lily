from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt

from app.dependencies import get_db
from app.models import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioOut, Token, RefreshTokenRequest
from app.core import security
from app.core.config import settings
from app.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/register", response_model=UsuarioOut, status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario_in: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existente = db.query(Usuario).filter(Usuario.email == usuario_in.email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    nuevo_usuario = Usuario(
        nombre=usuario_in.nombre,
        email=usuario_in.email,
        hashed_password=security.hash_password(usuario_in.password),
        acepto_tratamiento=usuario_in.acepto_tratamiento,
        fecha_consentimiento=datetime.now(timezone.utc),
        rol="customer"
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == form_data.username).first()
    if not usuario or not security.verificar_password(form_data.password, usuario.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_expires = timedelta(minutes=settings.ACCESS_MIN)
    refresh_expires = timedelta(minutes=settings.REFRESH_MIN)

    access_token = security.crear_token(
        data={"sub": usuario.email, "rol": usuario.rol, "tipo": "access"},
        expires_delta=access_expires
    )
    refresh_token = security.crear_token(
        data={"sub": usuario.email, "rol": usuario.rol, "tipo": "refresh"},
        expires_delta=refresh_expires
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.get("/me", response_model=UsuarioOut)
def obtener_perfil(current_user: Usuario = Depends(get_current_user)):
    return current_user

@router.post("/refresh", response_model=Token)
def refrescar_token(body: RefreshTokenRequest, db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token de refresco inválido o expirado"
    )
    try:
        payload = jwt.decode(body.refresh_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        tipo: str = payload.get("tipo")
        if email is None or tipo != "refresh":
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        raise credentials_exception

    access_expires = timedelta(minutes=settings.ACCESS_MIN)
    refresh_expires = timedelta(minutes=settings.REFRESH_MIN)

    nuevo_access = security.crear_token(
        data={"sub": usuario.email, "rol": usuario.rol, "tipo": "access"},
        expires_delta=access_expires
    )
    nuevo_refresh = security.crear_token(
        data={"sub": usuario.email, "rol": usuario.rol, "tipo": "refresh"},
        expires_delta=refresh_expires
    )

    return {
        "access_token": nuevo_access,
        "refresh_token": nuevo_refresh,
        "token_type": "bearer"
    }

