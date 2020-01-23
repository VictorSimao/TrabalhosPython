#----- Importar biblioteca do Mysql
import MySQLdb
from model.squad import Squad

class SquadDao:

    def __init__(self):
        #----- Configurar a conexão
        self.conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans19', user='padawans19', passwd='vt2019')
        #----- Salva o cursor da conexão em uma variável
        self.cursor = self.conexao.cursor()

    def listar_todos(self):
        #----- Criação do comando SQL e passado para o cursor
        comando_sql_select = "SELECT * FROM SQUADS, BACKEND WHERE SQUADS.L_BACKEND_ID = BACKEND.ID"
        # "SELECT * FROM SQUADS AS S LEFT JOIN BACKEND AS B ON S.L_BACKEND_ID = B.ID"
        # SELECT * FROM 01_MDG_PESSOA AS P LEFT JOIN 01_MDG_ENDERECO AS E ON P.ENDERECO_ID = E.ID
        self.cursor.execute(comando_sql_select)
        #---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_por_id(self, id):
        #----- Criação do comando SQL e passado para o cursor
        comando = f"SELECT * FROM SQUADS WHERE IDS= {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
        comando = f""" INSERT INTO SQUADS
        (
            NOME,
            DESCRICAO,
            NUMEROPESSOAS,
            LINGUAGEMBACKEND,
            FRAMEWORKFRONTEND
        )
        VALUES
        (
            '{squad.nome}',
            '{squad.descricao}',
            {squad.numeropessoas},
            '{squad.linguagembackend}',
            '{squad.frameworkfrontend}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido
    
    def alterar(self, squad:Squad):
        comando = f""" UPDATE SQUADS
        SET
            NOME = '{squad.nome}',
            DESCRICAO ='{squad.descricao}',
            NUMEROPESSOAS = {squad.numeropessoas},
            LINGUAGEMBACKEND = '{squad.linguagembackend}',
            FRAMEWORKFRONTEND = '{squad.frameworkfrontend}'
        WHERE ID = {squad.idsquad}
        """
        self.cursor.execute(comando)
        self.conexao.commit()
    
    def deletar(self, id):
        comando = f"DELETE FROM SQUADS WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()