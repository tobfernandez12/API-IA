import psycopg
from models.modelos import Destino

class destinoManager:

    def obtener_destinos(self, cursor: psycopg.Cursor):
        cursor.execute("SELECT * FROM destino")
        return cursor.fetchall()

    def obtener_destino_por_id(self, id: int, cursor: psycopg.Cursor):
        cursor.execute("SELECT * FROM destino WHERE id = %s", (id,))
        return cursor.fetchone()
    
    def buscar_destino_por_nombre(self, nombre: str, cursor: psycopg.Cursor):
        cursor.execute("SELECT * FROM destino WHERE nombre = %s", (nombre,))
        return cursor.fetchall()

    def buscar_destino_por_pais(self, pais: str, cursor: psycopg.Cursor):
        cursor.execute("SELECT * FROM destino WHERE pais = %s", (pais,))
        return cursor.fetchall()

    def crear_destino(self, destino: Destino, cursor: psycopg.Cursor):
        cursor.execute("INSERT INTO destino (nombre, pais) VALUES (%s, %s)",
            (destino.nombre, destino.pais))
        return {"mensaje": "Destino creado"}

    def modificar_destino(self, id: int, destino: Destino, cursor: psycopg.Cursor):
        cursor.execute("UPDATE destino SET nombre = %s, pais = %s WHERE id = %s",
            (destino.nombre, destino.pais, id))
        return {"mensaje": "Destino modificado"}

    def eliminar_destino(self, id: int, cursor: psycopg.Cursor):
        cursor.execute("DELETE FROM destino WHERE id = %s", (id,))
        return {"mensaje": "Destino eliminado"}

     
    def crear_destino_por_usuario(self, nombre_usuario: str, destino: Destino, cursor: psycopg.Cursor):
        cursor.execute("SELECT id FROM usuario WHERE nombre = %s", (nombre_usuario,))
        usuario = cursor.fetchone()
        if not usuario:
            return {"error": f"Usuario '{nombre_usuario}' no encontrado"}
        
        id_usuario = usuario[0]
        cursor.execute("""
            INSERT INTO destino (nombre, pais, id_usuario)
            VALUES (%s, %s, %s)
        """, (destino.nombre, destino.pais, id_usuario))
        return {"mensaje": f"Destino agregado al usuario {nombre_usuario}"}

    
    def obtener_destinos_por_usuario(self, nombre_usuario: str, cursor: psycopg.Cursor):
        cursor.execute("""
            SELECT d.*
            FROM destino d
            JOIN usuario u ON d.id_usuario = u.id
            WHERE u.nombre = %s
        """, (nombre_usuario,),)
        return cursor.fetchall()
    