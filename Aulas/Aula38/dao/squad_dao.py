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
        # "SELECT * FROM SQUADS S LEFT JOIN BACKEND AS B ON S.L_BACKEND_ID = B.ID"
        # SELECT * FROM 01_MDG_PESSOA AS P LEFT JOIN 01_MDG_ENDERECO AS E ON P.ENDERECO_ID = E.ID

        comando_sql_select = "SELECT * FROM SQUADS"
        self.cursor.execute(comando_sql_select)
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
        )
        VALUES
        (
            '{squad.nome}',
            '{squad.descricao}',
            {squad.numeropessoas},
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
        WHERE ID = {squad.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()
    
    def deletar(self, id):
        comando = f"DELETE FROM SQUADS WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()