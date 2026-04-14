import os
from .models import Usuario
import mysql.connector

class UsuarioDAO:
    def __init__(self):
        self.__db_config = {
            'host': os.getenv("MYSQL_HOST"),
            'user': os.getenv("MYSQL_USER"),
            'password': os.getenv("MYSQL_PASSWORD"),
            'database': os.getenv("MYSQL_DATABASE"),
            'port': os.getenv("MYSQL_PORT")
        }

    def __get_connection(self):
        return mysql.connector.connect(**self.__db_config)

    def salvar_usuario(self, usuario):
        try:
            sql = "INSERT INTO usuarios(nome, email, senha) VALUES (%s, %s, %s)"
            valores = (usuario.nome, usuario.email, usuario.senha)
            conexao = self.__get_connection()
            cursor = conexao.cursor()
            cursor.execute(sql, valores)
            conexao.commit()
            usuario.id = cursor.lastrowid
        except mysql.connector.Error as e:
            print(f"Erro ao salvar usuário: {e}")
            raise
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexao' in locals():
                conexao.close()

    def buscar_por_email(self, email):
        try:
            sql = "SELECT * FROM usuarios WHERE email = %s"
            conexao = self.__get_connection()
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(sql, (email,))
            linha = cursor.fetchone()
            if linha:
                return Usuario(
                    linha["nome"], linha["email"], linha["senha"],
                    usuario_id=linha["id"]
                )
        except mysql.connector.Error as e:
            print(f"Erro ao buscar usuário por email: {e}")
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexao' in locals():
                conexao.close()
        return None

    def buscar_por_id(self, usuario_id):
        try:
            sql = "SELECT id, nome, email, senha FROM usuarios WHERE id = %s"
            conexao = self.__get_connection()
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(sql, (usuario_id,))
            linha = cursor.fetchone()
            if linha:
                return Usuario(
                    linha["nome"], linha["email"], linha["senha"],
                    usuario_id=linha["id"]
                )
        except mysql.connector.Error as e:
            print(f"Erro ao buscar usuário por id: {e}")
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexao' in locals():
                conexao.close()
        return None