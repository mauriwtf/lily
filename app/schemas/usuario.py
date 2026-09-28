from pydantic import BaseModel, EmailStr, ConfigDict, field_validator
from typing import Optional
from datetime import datetime

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str
    acepto_tratamiento: bool

    @field_validator("acepto_tratamiento")
    @classmethod
    def validar_consentimiento(cls, v: bool) -> bool:
        if not v:
            raise ValueError("Debe aceptar el tratamiento de datos personales para registrarse.")
        return v

class UsuarioOut(UsuarioBase):
    id: int
    rol: str
    acepto_tratamiento: bool
    fecha_consentimiento: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class RefreshTokenRequest(BaseModel):
    refresh_token: str