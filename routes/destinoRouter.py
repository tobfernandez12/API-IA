import psycopg
from fastapi import APIRouter, Depends
from models.modelos import Destino
from managers.destinoManager import destinoManager
from managers.conexionManagerSupabase import getCursor

router = APIRouter(prefix="/destinos", tags=["Rutas de Destinos"])
manager = destinoManager()

@router.get("/obtener_destinos")
def obtener_destinos(cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.obtener_destinos(cursor)

@router.get("/obtener_destino/{id}")
def obtener_destino_por_id(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.obtener_destino_por_id(id, cursor)

@router.get("/buscar_por_nombre/{nombre}")
def buscar_por_nombre(nombre: str, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.buscar_destino_por_nombre(nombre, cursor)

@router.get("/buscar_por_pais/{pais}")
def buscar_por_pais(pais: str, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.buscar_destino_por_pais(pais, cursor)

@router.post("/usuario/{nombre_usuario}/destino")
def crear_destino(nombre_usuario: str, destino: Destino, cursor=Depends(getCursor)):
    return manager.crear_destino_por_usuario(nombre_usuario, destino, cursor)

@router.get("/usuario/{nombre_usuario}/destinos")
def obtener_destinos(nombre_usuario: str, cursor=Depends(getCursor)):
    return manager.obtener_destinos_por_usuario(nombre_usuario, cursor)


@router.put("/modificar_destino/{id}")
def modificar_destino(id: int, destino: Destino, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.modificar_destino(id, destino, cursor)

@router.delete("/eliminar_destino/{id}")
def eliminar_destino(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.eliminar_destino(id, cursor)