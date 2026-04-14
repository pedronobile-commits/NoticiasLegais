import os
from .models import Noticia
import mysql.connector

class NoticiaDAO:
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

    def carregar_noticias(self):
        try:
            sql = "SELECT id, titulo, autor, conteudo, data_publicacao, categoria, fonte, imagem FROM noticias"
            lista = []
            conexao = self.__get_connection()
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(sql)
            for linha in cursor.fetchall():
                imagem_valor = linha["imagem"]
                if isinstance(imagem_valor, (bytes, bytearray)):
                    imagem_valor = imagem_valor.decode("utf-8", errors="ignore")

                noticia = Noticia(
                    linha["titulo"], linha["autor"], linha["conteudo"], 
                    linha["data_publicacao"], linha["categoria"], linha["fonte"], imagem_valor, 
                    noticia_id=linha["id"]
                )
                lista.append(noticia)
            return lista
        except mysql.connector.Error as e:
            print(f"Erro ao carregar notícias: {e}")
            return []
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexao' in locals():
                conexao.close()

    def buscar_por_titulo(self, titulo):
        try:
            sql = """
                SELECT id, titulo, autor, conteudo, data_publicacao, categoria, fonte, imagem 
                FROM noticias 
                WHERE LOWER(titulo) LIKE LOWER(%s)
            """
            lista = []
            conexao = self.__get_connection()
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(sql, (f'%{titulo}%',))
            for linha in cursor.fetchall():
                imagem_valor = linha["imagem"]
                if isinstance(imagem_valor, (bytes, bytearray)):
                    imagem_valor = imagem_valor.decode("utf-8", errors="ignore")

                noticia = Noticia(
                    linha["titulo"], linha["autor"], linha["conteudo"], 
                    linha["data_publicacao"], linha["categoria"], linha["fonte"], imagem_valor, 
                    noticia_id=linha["id"]
                )
                lista.append(noticia)
            return lista
        except mysql.connector.Error as e:
            print(f"Erro ao buscar notícias por título: {e}")
            return []
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexao' in locals():
                conexao.close()

    def salvar_noticia(self, noticia):
        try:
            sql = "INSERT INTO noticias(titulo, autor, conteudo, data_publicacao, categoria, fonte, imagem) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            valores = (noticia.titulo, noticia.autor, noticia.conteudo, noticia.data_publicacao, noticia.categoria, noticia.fonte, noticia.imagem)
            conexao = self.__get_connection()
            cursor = conexao.cursor()
            cursor.execute(sql, valores)
            conexao.commit()
            noticia.id = cursor.lastrowid
        except mysql.connector.Error as e:
            print(f"Erro ao salvar notícia: {e}")
            raise
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexao' in locals():
                conexao.close()

    def buscar_por_id(self, id_noticia):
        try:
            sql = "SELECT * FROM noticias WHERE id = %s"
            conexao = self.__get_connection()
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(sql, (id_noticia,))
            linha = cursor.fetchone()
            if linha:
                imagem_valor = linha["imagem"]
                if isinstance(imagem_valor, (bytes, bytearray)):
                    imagem_valor = imagem_valor.decode("utf-8", errors="ignore")

                return Noticia(
                    linha["titulo"], linha["autor"], linha["conteudo"], 
                    linha["data_publicacao"], linha["categoria"], linha["fonte"], imagem_valor,
                    noticia_id=linha["id"]
                )
        except mysql.connector.Error as e:
            print(f"Erro ao buscar notícia por ID: {e}")
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexao' in locals():
                conexao.close()
        return None

    def atualizar_noticia(self, noticia):
        try:
            sql = "UPDATE noticias SET titulo=%s, autor=%s, conteudo=%s, data_publicacao=%s, categoria=%s, fonte=%s, imagem=%s WHERE id=%s"
            valores = (noticia.titulo, noticia.autor, noticia.conteudo, noticia.data_publicacao, noticia.categoria, noticia.fonte, noticia.imagem, noticia.id)
            conexao = self.__get_connection()
            cursor = conexao.cursor()
            cursor.execute(sql, valores)
            conexao.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao atualizar notícia: {e}")
            raise
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexao' in locals():
                conexao.close()

    def remover_noticia(self, id_noticia):
        try:
            sql = "DELETE FROM noticias WHERE id = %s"
            conexao = self.__get_connection()
            cursor = conexao.cursor()
            cursor.execute(sql, (id_noticia,))
            conexao.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao remover notícia: {e}")
            raise
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexao' in locals():
                conexao.close()
