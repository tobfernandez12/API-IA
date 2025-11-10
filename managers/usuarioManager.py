import psycopg
from models.modelos import Usuario

class usuarioManager:

    def obtener_usuarios(self, cursor: psycopg.Cursor):
        cursor.execute("SELECT * FROM usuario")
        return cursor.fetchall()

    def obtener_usuario_por_id(self, id: int, cursor: psycopg.Cursor):
        cursor.execute("SELECT * FROM usuario WHERE id = %s", (id,))
        return cursor.fetchone()
    
    def buscar_usuario_por_nombre(self, nombre: str, cursor: psycopg.Cursor):
        cursor.execute("SELECT * FROM usuario WHERE nombre = %s", (nombre,))
        return cursor.fetchall()

    def buscar_usuario_por_nacionalidad(self, nacionalidad: str, cursor: psycopg.Cursor):
        cursor.execute("SELECT * FROM usuario WHERE nacionalidad = %s", (nacionalidad,))
        return cursor.fetchall()
    
    def crear_usuario(self, usuario: Usuario, cursor: psycopg.Cursor):
        cursor.execute("INSERT INTO usuario (nombre, nacionalidad) VALUES (%s, %s)",
            (usuario.nombre, usuario.nacionalidad))
        return {"mensaje": "Usuario creado"}

    def modificar_usuario(self, id: int, usuario: Usuario, cursor: psycopg.Cursor):
        cursor.execute("UPDATE usuario SET nombre = %s, nacionalidad = %s WHERE id = %s",
            (usuario.nombre, usuario.nacionalidad, id))
        return {"mensaje": "Usuario modificado"}

    def eliminar_usuario(self, id: int, cursor: psycopg.Cursor):
        cursor.execute("DELETE FROM usuario WHERE id = %s", (id,))
        return {"mensaje": "Usuario eliminado"}
