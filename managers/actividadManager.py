import psycopg
from models.modelos import Actividad

class actividadManager:

    def obtener_actividades(self, cursor: psycopg.Cursor):
        cursor.execute("SELECT * FROM actividad")
        return cursor.fetchall()

    def obtener_actividad_por_id(self, id: int, cursor: psycopg.Cursor):
        cursor.execute("SELECT * FROM actividad WHERE id = %s", (id,))
        return cursor.fetchone()
    
    def buscar_actividad_por_nombre(self, nombre: str, cursor: psycopg.Cursor):
        cursor.execute("SELECT * FROM actividad WHERE nombre = %s", (nombre,))
        return cursor.fetchall()

    def buscar_actividad_por_descripcion(self, descripcion: str, cursor: psycopg.Cursor):
        cursor.execute("SELECT * FROM actividad WHERE descripcion = %s", (descripcion,))
        return cursor.fetchall()
    
    def crear_actividad(self, actividad: Actividad, cursor: psycopg.Cursor):
        cursor.execute("INSERT INTO actividad (nombre, descripcion) VALUES (%s, %s)",
            (actividad.nombre, actividad.descripcion))
        return {"mensaje": "Actividad creada"}
    
    def modificar_actividad(self, id: int, actividad: Actividad, cursor: psycopg.Cursor):
        cursor.execute("UPDATE actividad SET nombre = %s, descripcion = %s WHERE id = %s",
            (actividad.nombre, actividad.descripcion, id))
        return {"mensaje": "Actividad modificada"}

    def eliminar_actividad(self, id: int, cursor: psycopg.Cursor):
        cursor.execute("DELETE FROM actividad WHERE id = %s", (id,))
        return {"mensaje": "Actividad eliminada"}

    def crear_actividad_por_usuario(self, nombre_usuario: str, actividad: Actividad, cursor: psycopg.Cursor):
        cursor.execute("SELECT id FROM usuario WHERE nombre = %s", (nombre_usuario,))
        usuario = cursor.fetchone()
        if not usuario:
            return {"error": f"Usuario '{nombre_usuario}' no encontrado"}
        
        id_usuario = usuario[0]
        cursor.execute("""
            INSERT INTO actividad (nombre, descripcion, id_usuario)
            VALUES (%s, %s, %s)
        """, (actividad.nombre, actividad.descripcion, id_usuario))
        return {"mensaje": f"Actividad agregada al usuario {nombre_usuario}"}

    
    def obtener_actividades_por_usuario(self, nombre_usuario: str, cursor: psycopg.Cursor):
        cursor.execute("""
            SELECT a.*
            FROM actividad a
            JOIN usuario u ON a.id_usuario = u.id
            WHERE u.nombre = %s
        """, (nombre_usuario,))
        return cursor.fetchall()