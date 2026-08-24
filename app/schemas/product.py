from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    id: int
    name: str = Field(..., description="Nombre del jugo o bebida")
    price: float = Field(..., description="Precio en Pesos Argentinos (ARS)")
    description: str = Field(..., description="Descripción de ingredientes y beneficios")

class Product(ProductBase):
    pass
