from sqlalchemy.orm import Session
from app.models import Producto
from app.schemas import ProductoCreate
from typing import Optional

def crear_producto(db: Session, producto: ProductoCreate):
    db_producto = Producto(**producto.model_dump())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def listar_productos(
    db: Session, 
    skip: int = 0, 
    limit: int = 10, 
    nombre: Optional[str] = None, 
    precio_max: Optional[float] = None
):
    query = db.query(Producto)
    
    # Filtro parcial por nombre (case-insensitive)
    if nombre:
        query = query.filter(Producto.nombre.ilike(f"%{nombre}%"))
        
    # Filtro por precio máximo
    if precio_max is not None:
        query = query.filter(Producto.precio <= precio_max)
        
    # Paginación con offset (skip) y límite (limit)
    return query.offset(skip).limit(limit).all()