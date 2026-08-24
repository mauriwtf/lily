from fastapi import APIRouter
from typing import List
from app.schemas.product import Product

router = APIRouter()

# Catálogo oficial de FreshMix en memoria
PRODUCTS_DB = [
    {
        "id": 1,
        "name": "Jugo de Naranja Natural",
        "price": 4500.0,
        "description": "100% naranja exprimida"
    },
    {
        "id": 2,
        "name": "Jugo Tropical",
        "price": 5200.0,
        "description": "Ananá, mango y maracuyá"
    },
    {
        "id": 3,
        "name": "Jugo Detox Verde",
        "price": 5500.0,
        "description": "Manzana, pepino, espinaca y limón"
    },
    {
        "id": 4,
        "name": "Jugo de Frutilla y Banana",
        "price": 5000.0,
        "description": "Bebida dulce y energética"
    },
    {
        "id": 5,
        "name": "Limonada con Menta",
        "price": 4800.0,
        "description": "Limón fresco y hojas de menta"
    }
]

@router.get("/", response_model=List[Product])
def get_products():
    """
    Retorna el catálogo oficial de FreshMix.
    """
    return PRODUCTS_DB
