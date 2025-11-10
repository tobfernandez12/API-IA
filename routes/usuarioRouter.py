import psycopg
from fastapi import APIRouter, Depends
from models.modelos import Usuario
from managers.usuarioManager import usuarioManager
from managers.conexionManagerSupabase import getCursor

router = APIRouter(prefix="/usuarios", tags=["Rutas de Usuarios"])
manager = usuarioManager()

@router.get("/obtener_usuarios")
def obtener_usuarios(cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.obtener_usuarios(cursor)

@router.get("/obtener_usuario/{id}")
def obtener_usuario_por_id(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.obtener_usuario_por_id(id, cursor)

@router.get("/buscar_por_nombre/{nombre}")
def buscar_por_nombre(nombre: str, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.buscar_usuario_por_nombre(nombre, cursor)

@router.get("/buscar_por_nacionalidad/{nacionalidad}")
def buscar_por_nacionalidad(nacionalidad: str, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.buscar_usuario_por_nacionalidad(nacionalidad, cursor)

@router.post("/crear_usuario")
def crear_usuario(usuario: Usuario, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.crear_usuario(usuario, cursor)

@router.put("/modificar_usuario/{id}")
def modificar_usuario(id: int, usuario: Usuario, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.modificar_usuario(id, usuario, cursor)

@router.delete("/eliminar_usuario/{id}")
def eliminar_usuario(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.eliminar_usuario(id, cursor)


