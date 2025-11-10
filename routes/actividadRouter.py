import psycopg
from fastapi import APIRouter, Depends
from models.modelos import Actividad
from managers.actividadManager import actividadManager
from managers.conexionManagerSupabase import getCursor

router = APIRouter(prefix="/actividades", tags=["Rutas de Actividades"])
manager = actividadManager()

@router.get("/obtener_actividades")
def obtener_actividades(cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.obtener_actividades(cursor)

@router.get("/obtener_actividad/{id}")
def obtener_actividad_por_id(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.obtener_actividad_por_id(id, cursor)

@router.get("/buscar_por_nombre/{nombre}")
def buscar_por_nombre(nombre: str, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.buscar_actividad_por_nombre(nombre, cursor)

@router.get("/buscar_por_descripcion/{descripcion}")
def buscar_por_descripcion(descripcion: str, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.buscar_actividad_por_descripcion(descripcion, cursor)

@router.post("/usuario/{nombre_usuario}/actividad")
def crear_actividad(nombre_usuario: str, actividad: Actividad, cursor=Depends(getCursor)):
    return manager.crear_actividad_por_usuario(nombre_usuario, actividad, cursor)

@router.put("/modificar_actividad/{id}")
def modificar_actividad(id: int, actividad: Actividad, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.modificar_actividad(id, actividad, cursor)

@router.delete("/eliminar_actividad/{id}")
def eliminar_actividad(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.eliminar_actividad(id, cursor)
