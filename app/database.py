import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# 1. Asegurar codificación
os.environ["PGCLIENTENCODING"] = "utf-8"

# 2. Forzar IP 127.0.0.1 en lugar de localhost para evitar problemas de IPv6 en Windows
url = str(settings.DATABASE_URL).replace("localhost", "127.0.0.1")

# Si la URL no coincide con las credenciales confirmadas, la aseguramos:
if "mauri420238" not in url:
    url = "postgresql://postgres:mauri420238@127.0.0.1:5432/ecommerce_db"

# Variable requerida por Alembic env.py
SQLALCHEMY_DATABASE_URL = url

print(f"--> Conectando a PostgreSQL con: {url.split('@')[-1]}")

engine = create_engine(
    url,
    connect_args={"client_encoding": "utf8"}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

