<<<<<<< HEAD
# API de Gestión de Usuarios, Destinos y Actividades

Esta API RESTful desarrollada con **FastAPI** y **inteligencia artificial** permite administrar usuarios, destinos y actividades.  
Incluye endpoints CRUD completos para cada entidad.
En esta API teníamos que utilizar inteligencia artificial, nosotros la utilizamos de la siguiente forma:
-Le consultamos a ChatGPT que nos brindé ideas para hacer una API 
-Luego, a medida que íbamos haciendo, le consultamos sobre nuestros errores y nos fue corrigiendo
-Por último, gran parte de este README.md esta hecho con IA (incluyendo imagen)

---
!(images/image.png)

#Tecnologías utilizadas

- Python 3  
- FastAPI  
- PostgreSQL  
- psycopg
- Uvicorn

---

#Estructura del proyecto

API/
┣routes/
┃ 	┣actividadRouter.py
┃ 	┣destinoRouter.py
┃ 	┗usuarioRouter.py
┣managers/
┃ 	┣actividadManager.py
┃ 	┣destinoManager.py
┃ 	┗usuarioManager.py
┣models/
┃ 	┗modelos.py
┣main.py
┣vercel.json
┗requirements.txt

## Endpoints

### Usuarios

| Método | Endpoint | Descripción |
|:--------|:----------|:-------------|
| GET | `/usuarios` | Obtener todos los usuarios |
| GET | `/usuarios/{id}` | Obtener un usuario por ID |
| POST | `/usuarios` | Crear un nuevo usuario |
| PUT | `/usuarios/{id}` | Modificar un usuario existente |
| DELETE | `/usuarios/{id}` | Eliminar un usuario |

### Destinos

| Método | Endpoint | Descripción |
|:--------|:----------|:-------------|
| GET | `/destinos` | Obtener todos los destinos |
| GET | `/destinos/{id}` | Obtener un destino por ID |
| GET | `/destinos/{id}` | Obtener un destino por Usuario |
| POST | `/destinos` | Crear un nuevo destino |
| POST | `/destinos` | Crear un nuevo destino por Usuario|
| PUT | `/destinos/{id}` | Modificar un destino existente |
| DELETE | `/destinos/{id}` | Eliminar un destino |

### Actividades

| Método | Endpoint | Descripción |
|:--------|:----------|:-------------|
| GET | `/actividades` | Obtener todas las actividades |
| GET | `/actividades/{id}` | Obtener una actividad por ID |
| POST | `/actividades` | Crear una nueva actividad por Usuario|
| PUT | `/actividades/{id}` | Modificar una actividad existente |
| DELETE | `/actividades/{id}` | Eliminar una actividad |

---

## Instalación y ejecución

```bash
# Clonar el repositorio
git clone https://github.com/tuusuario/tu-repo.git
cd tu-repo

# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el servidor
uvicorn main:app --reload
=======
# API-IA
Realizamos una API de una agencia de turismo con ayuda de Inteligencia Artifical (ChatGPT)
>>>>>>> ab06e94e19e8a2b9cf1bce00f7e8ad032cdbbbba
