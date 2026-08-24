from fastapi import FastAPI
from app.routers import products, cart

app = FastAPI(
    title="FreshMix API",
    version="1.0.0",
    description="API de FreshMix para el e-commerce de jugos naturales y bebidas saludables."
)

@app.get("/")
def read_root():
    """
    Endpoint de bienvenida que detalla las políticas y cumplimiento
    de las normativas de consumo en la República Argentina.
    """
    return {
        "marca": "FreshMix",
        "eslogan": "Sabor natural en cada sorbo",
        "ubicacion": "Villa Carlos Paz, Cordoba, Argentina",
        "mensaje": "Bienvenido a la API oficial de FreshMix. Descubri nuestras bebidas saludables.",
        "cumplimiento_legal": {
            "ley_24240_defensa_consumidor": (
                "En cumplimiento con la Ley N° 24.240 de Defensa del Consumidor de la Republica Argentina, "
                "garantizamos el derecho a la informacion clara, detallada y veraz sobre las caracteristicas, "
                "precios y condiciones de nuestros productos."
            ),
            "resolucion_424_2020_arrepentimiento": (
                "Conforme a la Resolucion 424/2020 de la Secretaria de Comercio Interior, "
                "se establece la obligacion de publicar un Boton de Arrepentimiento. "
                "El consumidor tiene derecho a revocar la aceptacion de la compra dentro de los 10 dias "
                "corridos contados a partir de la entrega del producto o de la celebracion del contrato sin responsabilidad alguna."
            ),
            "ley_25326_proteccion_datos": (
                "De acuerdo con la Ley N° 25.326 de Proteccion de Datos Personales, nos comprometemos a "
                "proteger la privacidad de sus datos y a utilizarlos estrictamente para procesar sus pedidos "
                "y mejorar su experiencia de usuario. El titular de los datos personales tiene la facultad de "
                "ejercer el derecho de acceso, rectificacion o supresion de los mismos."
            )
        }
    }

# Incluir routers
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(cart.router, prefix="/cart", tags=["Cart"])
