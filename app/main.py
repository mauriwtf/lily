from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="FreshMix API")

# Habilitar CORS para conectar con React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Paso 1: Modelo Producto con Pydantic
class Producto(BaseModel):
    id: int
    nombre: str
    precio_final: float
    cuotas_cantidad: int
    cuotas_valor: float
    garantia_meses: int
    stock: int

# Paso 2: Lista en memoria con 3 productos
productos_db: list[Producto] = [
    Producto(
        id=1,
        nombre="Jugo de Naranja Natural",
        precio_final=4500.0,
        cuotas_cantidad=3,
        cuotas_valor=1500.0,
        garantia_meses=1,
        stock=50
    ),
    Producto(
        id=2,
        nombre="Jugo Tropical",
        precio_final=5200.0,
        cuotas_cantidad=3,
        cuotas_valor=1733.33,
        garantia_meses=1,
        stock=30
    ),
    Producto(
        id=3,
        nombre="Jugo Detox Verde",
        precio_final=5500.0,
        cuotas_cantidad=3,
        cuotas_valor=1833.33,
        garantia_meses=1,
        stock=25
    )
]

# Paso 3: Endpoint GET /productos
@app.get("/productos", response_model=list[Producto])
def obtener_productos():
    return productos_db

# Paso 4: Endpoint POST /productos
@app.post("/productos", response_model=Producto, status_code=201)
def crear_producto(producto: Producto):
    productos_db.append(producto)
    return producto