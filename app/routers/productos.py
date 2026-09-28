from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.dependencies import get_db, require_admin
from app import schemas
from app.services import productos as service_productos

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post("/", response_model=schemas.ProductoOut, dependencies=[Depends(require_admin)])
def crear(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return service_productos.crear_producto(db=db, producto=producto)

@router.get("/", response_model=List[schemas.ProductoOut])
def listar(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    nombre: Optional[str] = None,
    precio_max: Optional[float] = None,
    db: Session = Depends(get_db)
):
    return service_productos.listar_productos(
        db=db, skip=skip, limit=limit, nombre=nombre, precio_max=precio_max
    )