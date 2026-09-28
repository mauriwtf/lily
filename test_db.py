import socket
import psycopg2
from app.core.config import settings

print("=== 1. ESCANEANDO PUERTOS DE POSTGRESQL ===")
puertos_activos = []
for port in [5432, 5433, 5434]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    if s.connect_ex(('127.0.0.1', port)) == 0:
        print(f" -> Encontrado servicio activo en el puerto: {port}")
        puertos_activos.append(port)
    s.close()

print("\n=== 2. PROBANDO CONEXIÓN A ECOMMERCE_DB ===")
for port in puertos_activos:
    url = f"postgresql://postgres:mauri420238@127.0.0.1:{port}/ecommerce_db"
    try:
        conn = psycopg2.connect(url)
        print(f"\n¡ÉXITO TOTAL! Tu base de datos responde en el puerto {port}")
        print(f"Copiá esta URL exacta a tu .env:\nDATABASE_URL={url}")
        conn.close()
        break
    except Exception:
        print(f" -> Puerto {port}: El servidor respondió pero rechazó el usuario/clave.")