# FreshMix Backend API
> **"Sabor natural en cada sorbo"** - E-commerce de jugos naturales y bebidas saludables en Villa Carlos Paz.

Este es el backend oficial de **FreshMix**, desarrollado utilizando Python y FastAPI. Cuenta con un diseño modular y estructurado que permite la gestion en memoria de un catalogo de jugos naturales y la simulacion de compras y escaneos de codigos QR para agilizar el carrito de compras.

---

## 🏛️ Cumplimiento Normativo (Argentina)

Esta aplicacion backend contempla de manera explicita las siguientes normativas argentinas de defensa del consumidor y privacidad de datos:

1. **Ley N° 24.240 (Defensa del Consumidor):** Garantizamos la transparencia de precios, descripcion detallada de ingredientes y terminos claros de comercializacion de todas las bebidas saludables.
2. **Secretaria de Comercio Interior - Resolucion N° 424/2020 (Boton de Arrepentimiento):** Se habilita y contempla el derecho de revocacion de la compra dentro de los 10 (diez) dias corridos a partir de la contratacion o recepcion del producto, sin cargos ni penalizaciones para el usuario.
3. **Ley N° 25.326 (Proteccion de Datos Personales):** Se garantiza que el tratamiento de datos personales de los clientes se realiza bajo estrictos estandares de seguridad y confidencialidad. Los usuarios disponen del derecho de acceso, rectificacion, actualizacion y eliminacion de sus datos.

---

## 📂 Estructura del Proyecto

El backend esta estructurado de forma limpia y escalable:

- `app/core/`: Centraliza archivos de configuracion global, seguridad y constantes de la aplicacion.
- `app/models/`: Contiene los modelos de persistencia (ORMs de bases de datos en futuras iteraciones).
- `app/schemas/`: Define los esquemas de validacion y serializacion de datos mediante Pydantic (data validation).
- `app/services/`: Concentra la logica de negocio y casos de uso principales desacoplados de los endpoints.
- `app/routers/`: Maneja las rutas HTTP (endpoints) y la comunicacion con los clientes de la API.
- `app/main.py`: Punto de entrada que inicializa FastAPI, configura los middleware e incluye las rutas del sistema.

---

## 🚀 Instrucciones para Correr el Servidor

Siga los siguientes pasos para ejecutar el proyecto de forma local:

### 1. Clonar o acceder al directorio del proyecto
```bash
cd freshmix
```

### 2. Crear y activar el entorno virtual
En Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
En macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Iniciar el servidor de desarrollo
Corra uvicorn apuntando a la aplicacion principal:
```bash
uvicorn app.main:app --reload
```

El servidor estara disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000).
Puede explorar la documentacion interactiva (Swagger UI) en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
