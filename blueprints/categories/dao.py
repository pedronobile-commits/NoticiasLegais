import os
from .models import Categoria
import mysql.connector

class CategoriaDAO:
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

    def salvar_categoria(self, categoria):
        try:
            sql = "INSERT INTO categorias(nome) VALUES (%s)"
            valores = (categoria.nome,)
            conexao = self.__get_connection()
            cursor = conexao.cursor()
            cursor.execute(sql, valores)
            conexao.commit()
            categoria.id = cursor.lastrowid
        except mysql.connector.Error as e:
            print(f"Erro ao salvar categoria: {e}")
            raise
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexao' in locals():
                conexao.close()

    def carregar_categorias(self):
        try:
            sql = "SELECT id, nome FROM categorias"
            lista = []
            conexao = self.__get_connection()
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(sql)
            for linha in cursor.fetchall():
                categoria = Categoria(
                    linha["nome"], categoria_id=linha["id"]
                )
                lista.append(categoria)
            return lista
        except mysql.connector.Error as e:
            print(f"Erro ao carregar categorias: {e}")
            return []
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexao' in locals():
                conexao.close()

    def buscar_por_nome(self, nome):
        try:
            sql = "SELECT * FROM categorias WHERE nome = %s"
            conexao = self.__get_connection()
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(sql, (nome,))
            linha = cursor.fetchone()
            if linha:
                return Categoria(
                    linha["nome"], categoria_id=linha["id"]
                )
            return None
        except mysql.connector.Error as e:
            print(f"Erro ao buscar categoria por nome: {e}")
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexao' in locals():
                conexao.close()

    def buscar_por_id(self, id_categoria):
        try:
            sql = "SELECT * FROM categorias WHERE id = %s"
            conexao = self.__get_connection()
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(sql, (id_categoria,))
            linha = cursor.fetchone()
            if linha:
                return Categoria(
                    linha["nome"], categoria_id=linha["id"]
                )
            return None
        except mysql.connector.Error as e:
            print(f"Erro ao buscar categoria por ID: {e}")
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexao' in locals():
                conexao.close()

    def atualizar_categoria(self, categoria):
        try:
            sql = "UPDATE categorias SET nome = %s WHERE id = %s"
            valores = (categoria.nome, categoria.id)
            conexao = self.__get_connection()
            cursor = conexao.cursor()
            cursor.execute(sql, valores)
            if cursor.rowcount == 0:
                raise Exception("Categoria não encontrada")
            conexao.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao atualizar categoria: {e}")
            raise
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexao' in locals():
                conexao.close()

    def remover_categoria(self, id_categoria):
        try:
            sql = "DELETE FROM categorias WHERE id = %s"
            conexao = self.__get_connection()
            cursor = conexao.cursor()
            cursor.execute(sql, (id_categoria,))
            if cursor.rowcount == 0:
                raise Exception("Categoria não encontrada")
            conexao.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao remover categoria: {e}")
            raise
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexao' in locals():
                conexao.close()

