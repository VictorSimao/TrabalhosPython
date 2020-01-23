#----- Importar biblioteca do Mysql
import MySQLdb
from model.frontend import FrontEnd

class FrontEndDao:

    def __init__(self):
        #----- Configurar a conexão
        self.conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans19', user='padawans19', passwd='vt2019')
        #----- Salva o cursor da conexão em uma variável
        self.cursor = self.conexao.cursor()

    def listar_todos(self):
        #----- Criação do comando SQL e passado para o cursor
        comando_sql_select = "SELECT * FROM FRONTEND"
        self.cursor.execute(comando_sql_select)
        #---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_por_id(self, id):
        #----- Criação do comando SQL e passado para o cursor
        comando = f"SELECT * FROM FRONTEND WHERE ID= {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, frontend: FrontEnd):
        comando = f""" INSERT INTO BACKEND
        (
            NOME,
            VERSAO
        )
        VALUES
        (
            '{frontend.nome}',
            '{frontend.versao}',
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido
    
    def alterar(self, frontend: FrontEnd):
        comando = f""" UPDATE FRONTEND
        SET
            NOME = '{frontend.nome}',
            VERSAO = '{frontend.versao}'
        WHERE ID = {frontend.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()
    
    def deletar(self, id):
        comando = f"DELETE FROM FRONTEND WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()