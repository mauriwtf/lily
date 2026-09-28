from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from app.database import Base


from sqlalchemy import Column, Integer, String, Boolean, DateTime
# ... imports existentes ...

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    rol = Column(String, default="customer")
    acepto_tratamiento = Column(Boolean, nullable=False, default=True)  # <-- AGREGAR ESTA LÍNEA
    fecha_consentimiento = Column(DateTime, nullable=True)
class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio_final = Column(Float, nullable=False)