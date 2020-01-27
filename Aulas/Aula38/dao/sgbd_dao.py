#----- Importar biblioteca do Mysql
import MySQLdb
from model.sgbd import Sgbd

class SgbdDao:

    def __init__(self):
        #----- Configurar a conexão
        self.conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans19', user='padawans19', passwd='vt2019')
        #----- Salva o cursor da conexão em uma variável
        self.cursor = self.conexao.cursor()

    def listar_todos(self):
        #----- Criação do comando SQL e passado para o cursor
        comando_sql_select = "SELECT * FROM SGBD"
        self.cursor.execute(comando_sql_select)
        #---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_por_squad(self, id):
        comando = f"SELECT SG.NOME FROM SGBD AS SG RIGHT JOIN RELACIONAMENTO AS R ON SG.ID = R.SGBD_ID RIGHT JOIN SQUADS AS S ON R.SQUAD_ID = S.ID WHERE S.ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_por_id(self, id):
        #----- Criação do comando SQL e passado para o cursor
        comando = f"SELECT * FROM SGBD WHERE ID= {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, sgbd: Sgbd):
        comando = f""" INSERT INTO SGBD
        (
            NOME,
            VERSAO
        )
        VALUES
        (
            '{sgbd.nome}',
            '{sgbd.versao}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido
    
    def alterar(self, sgbd: Sgbd):
        comando = f""" UPDATE SGBD
        SET
            NOME = '{sgbd.nome}',
            VERSAO = '{sgbd.versao}'
        WHERE ID = {sgbd.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()
    
    def deletar(self, id):
        comando = f"DELETE FROM SGBD WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()