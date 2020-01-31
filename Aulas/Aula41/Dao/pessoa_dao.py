import MySQLdb
from Aulas.Aula41.Model.pessoa_model import PessoaModel

class PessoaDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', password='ts2019')
        self.cursor = self.connection.cursor()

    def list_all(self):
        self.cursor.execute("SELECT * FROM 01_MDG_PESSOA")
        lista_pessoa = []
        pessoas = self.cursor.fetchall()
        for p in pessoas:
            pessoa = PessoaModel(p[1], p[2], p[3], p[0])
            lista_pessoa.append(pessoa.__dict__m)
        return lista_pessoa

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM 01_MDG_PESSOA WHERE ID = {}".format(id))
        pessoa = self.cursor.fetchone()
        p1 = PessoaModel(pessoa[1],pessoa[2],pessoa[3],pessoa[0])
        return p1.__dict__

    def insert(self, pessoa):
        return 'Cadastrando uma pessoa : {}' .format(pessoa)

    def update(self, pessoa):
        return 'Alterando uma pessoa : {}' .format(pessoa)

    def remove(self, id):
        self.cursor.execute("DELETE FROM 01_MDG_PESSOA WHERE ID = {}".format(id))
        self.connection.commit()
        return 'Removido a pessoa de id: {}'.format(id)
