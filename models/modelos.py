from pydantic import BaseModel

class Actividad(BaseModel):
    nombre: str
    descripcion: str
    nombre_usuario: str
    id_usuario: int

class Destino(BaseModel):
    nombre: str
    pais: str
    nombre_usuario: str
    id_usuario: int

class Usuario(BaseModel):
    nombre: str
    nacionalidad: str