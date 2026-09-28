from pydantic import BaseModel
from typing import Optional

# --- Esquemas de Producto ---
class ProductoBase(BaseModel):
    nombre: str
    precio_final: float

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    precio_final: Optional[float] = None

class ProductoResponse(ProductoBase):
    id: int

    model_config = {"from_attributes": True}

# Alias para que coincida con los routers que usan ProductoOut
ProductoOut = ProductoResponse


# --- Esquemas de Usuario y Autenticación ---
class UsuarioBase(BaseModel):
    email: str
    nombre: str

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioResponse(UsuarioBase):
    id: int
    rol: str

    model_config = {"from_attributes": True}

# Alias para routers que usan UsuarioOut
UsuarioOut = UsuarioResponse

class Token(BaseModel):
    access_token: str
    token_type: str