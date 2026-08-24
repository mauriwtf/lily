from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from app.routers.products import PRODUCTS_DB

router = APIRouter()

# Carrito de compras temporal en memoria
cart_db: List[Dict[str, Any]] = []

class QRAddRequest(BaseModel):
    qr_payload: str  # Ejemplo: "3", "freshmix:product:3", "product-3"

@router.post("/qr-add")
def add_from_qr(payload_data: QRAddRequest):
    """
    Simula la adición al carrito escaneando un código QR en un local o folleto físico.
    Extrae el ID del producto desde el payload y lo agrega al carrito en memoria.
    """
    payload = payload_data.qr_payload.strip()
    
    # Intentamos extraer el ID del producto del código QR
    product_id = None
    if payload.isdigit():
        product_id = int(payload)
    elif "product:" in payload:
        try:
            product_id = int(payload.split("product:")[-1])
        except ValueError:
            pass
    elif "product-" in payload:
        try:
            product_id = int(payload.split("product-")[-1])
        except ValueError:
            pass
            
    if product_id is None:
        raise HTTPException(
            status_code=400,
            detail="Formato de QR no válido. Debe ser el ID del producto directo o contener 'product:<id>' o 'product-<id>'."
        )
        
    # Buscar el producto en el catálogo oficial
    product = next((p for p in PRODUCTS_DB if p["id"] == product_id), None)
    if not product:
        raise HTTPException(
            status_code=404,
            detail=f"Producto con ID {product_id} no encontrado en el catálogo oficial."
        )
        
    # Agregar al carrito
    cart_db.append(product)
    
    return {
        "message": f"Producto '{product['name']}' agregado al carrito mediante escaneo QR.",
        "added_product": product,
        "cart_total_items": len(cart_db),
        "cart": cart_db
    }

@router.get("/")
def get_cart():
    """
    Retorna el contenido del carrito actual y el total acumulado.
    """
    return {
        "items": cart_db,
        "total": sum(item["price"] for item in cart_db)
    }
