#----- Importar biblioteca do Mysql
import MySQLdb
from model.squad import Squad

class SquadDao:

    def __init__(self):
        self.conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans19', user='padawans19', passwd='vt2019')
        self.cursor = self.conexao.cursor()

    def listar_todos(self):
        comando_sql_select = "SELECT * FROM SQUADS"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_por_id(self, id):
        comando = f"SELECT * FROM SQUADS WHERE IDS= {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
        comando = f"INSERT INTO SQUADS (NOME,DESCRICAO,NUMERO_PESSOAS)VALUES('{squad.nome}','{squad.descricao}',{squad.numpessoas})"
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        squad.id = id_inserido
        for x in range(len(squad.backend)):
            if squad.backend[x] != None:
                comando1 = f"INSERT INTO RELACIONAMENTO (SQUAD_ID,BACK_ID)VALUES({squad.id},{squad.backend[x]})"
                self.cursor.execute(comando1)
                self.conexao.commit()
        for x in range(len(squad.frontend)):
            if squad.frontend[x] != None:
                comando2 = f"INSERT INTO RELACIONAMENTO (SQUAD_ID,FRONT_ID)VALUES({squad.id},{squad.frontend[x]})"
                self.cursor.execute(comando2)
                self.conexao.commit()
        for x in range(len(squad.sgbd)):
            if squad.sgbd[x] != None:
                comando3 = f"INSERT INTO RELACIONAMENTO (SQUAD_ID,SGBD_ID)VALUES({squad.id},{squad.sgbd[x]})"
                self.cursor.execute(comando3)
                self.conexao.commit()
        return id_inserido
    
    def alterar(self, squad:Squad):
        comando = f" UPDATE SQUADS SET NOME = '{squad.nome}', DESCRICAO = '{squad.descricao}', NUMERO_PESSOAS = {squad.numpessoas} WHERE ID = {squad.id}"
        self.cursor.execute(comando)
        self.conexao.commit()
        comando4 = f"DELETE FROM RELACIONAMENTO WHERE SQUAD_ID = {squad.id}"
        self.cursor.execute(comando4)
        self.conexao.commit()
        for x in range(len(squad.backend)):
            if squad.backend[x] != None:
                comando1 = f"INSERT INTO RELACIONAMENTO (SQUAD_ID,BACK_ID)VALUES({squad.id},{squad.backend[x]})"
                self.cursor.execute(comando1)
                self.conexao.commit()
        for x in range(len(squad.frontend)):
            if squad.frontend[x] != None:
                comando2 = f"INSERT INTO RELACIONAMENTO (SQUAD_ID,FRONT_ID)VALUES({squad.id},{squad.frontend[x]})"
                self.cursor.execute(comando2)
                self.conexao.commit()
        for x in range(len(squad.sgbd)):
            if squad.sgbd[x] != None:
                comando3 = f"INSERT INTO RELACIONAMENTO (SQUAD_ID,SGBD_ID)VALUES({squad.id},{squad.sgbd[x]})"
                self.cursor.execute(comando3)
                self.conexao.commit()
    
    def deletar(self, id):
        comando4 = f"DELETE FROM RELACIONAMENTO WHERE SQUAD_ID = {id}"
        self.cursor.execute(comando4)
        self.conexao.commit()
        comando = f"DELETE FROM SQUADS WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()