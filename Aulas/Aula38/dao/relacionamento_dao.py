import MySQLdb

class RelacionamentoDao:

    def __init__(self):
        #----- Configurar a conexão
        self.conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans19', user='padawans19', passwd='vt2019')
        #----- Salva o cursor da conexão em uma variável
        self.cursor = self.conexao.cursor()

    def salvar_back(self, squad:Squad):
        for i in range(0,2):
            comando = f""" INSERT INTO RELACIONAMENTO
            (
                SQUAD_ID,
                BACK_ID,
            )
            VALUES
            (
                {squad.id},
                {squad.backend[i]}
            )"""
            self.cursor.execute(comando)
            self.conexao.commit()
    
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