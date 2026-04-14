import os
from .models import Favorita
import mysql.connector

class FavoritaDAO:
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

    def adicionar_favorita(self, favorita):
        try:
            sql = "INSERT INTO favoritas(usuario_id, noticia_id) VALUES (%s, %s)"
            valores = (favorita.usuario_id, favorita.noticia_id)
            conexao = self.__get_connection()
            cursor = conexao.cursor()
            cursor.execute(sql, valores)
            conexao.commit()
            favorita.id = cursor.lastrowid
        except mysql.connector.Error as e:
            print(f"Erro ao adicionar favorita: {e}")
            raise
        finally:
            if 'conexao' in locals():
                conexao.close()

    def remover_favorita(self, usuario_id, noticia_id):
        try:
            sql = "DELETE FROM favoritas WHERE usuario_id = %s AND noticia_id = %s"
            valores = (usuario_id, noticia_id)
            conexao = self.__get_connection()
            cursor = conexao.cursor()
            cursor.execute(sql, valores)
            conexao.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao remover favorita: {e}")
            raise
        finally:
            if 'conexao' in locals():
                conexao.close()

    def is_favorita(self, usuario_id, noticia_id):
        try:
            sql = "SELECT id FROM favoritas WHERE usuario_id = %s AND noticia_id = %s"
            valores = (usuario_id, noticia_id)
            conexao = self.__get_connection()
            cursor = conexao.cursor()
            cursor.execute(sql, valores)
            resultado = cursor.fetchone()
            return resultado is not None
        except mysql.connector.Error as e:
            print(f"Erro ao verificar favorita: {e}")
            return False
        finally:
            if 'conexao' in locals():
                conexao.close()

    def listar_favoritas_por_usuario(self, usuario_id):
        try:
            sql = """
                SELECT n.id, n.titulo, n.autor, n.conteudo, n.data_publicacao, n.categoria, n.fonte, n.imagem
                FROM noticias n
                INNER JOIN favoritas f ON n.id = f.noticia_id
                WHERE f.usuario_id = %s
                ORDER BY n.data_publicacao DESC
            """
            lista = []
            conexao = self.__get_connection()
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(sql, (usuario_id,))
            for linha in cursor.fetchall():
                imagem_valor = linha["imagem"]
                if isinstance(imagem_valor, (bytes, bytearray)):
                    imagem_valor = imagem_valor.decode("utf-8", errors="ignore")

                from ..books.models import Noticia
                noticia = Noticia(
                    linha["titulo"], linha["autor"], linha["conteudo"], 
                    linha["data_publicacao"], linha["categoria"], linha["fonte"], imagem_valor, 
                    noticia_id=linha["id"]
                )
                lista.append(noticia)
            return lista
        except mysql.connector.Error as e:
            print(f"Erro ao listar favoritas: {e}")
            return []
        finally:
            if 'conexao' in locals():
                conexao.close()