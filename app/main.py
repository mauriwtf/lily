from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.routers import productos, auth
from app.database import engine, Base

from app import models  # <-- IMPORTANTE: importar los modelos para que SQLAlchemy los registre

Base.metadata.create_all(bind=engine)

# Esta línea crea las tablas automáticamente en PostgreSQL al arrancar
Base.metadata.create_all(bind=engine)
app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(productos.router)