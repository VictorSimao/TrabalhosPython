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
            lista_pessoa.append(pessoa.__dict__)
        return lista_pessoa

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM 01_MDG_PESSOA WHERE ID = {}".format(id))
        pessoa = self.cursor.fetchone()
        p1 = PessoaModel(pessoa[1],pessoa[2],pessoa[3],pessoa[0])
        return p1.__dict__

    def insert(self, pessoa:PessoaModel):
        self.cursor.execute("INSERT INTO 01_MDG_PESSOA (NOME, SOBRENOME, IDADE) VALUES('{}','{}','{}')".format(pessoa.nome, pessoa.sobrenome, pessoa.idade))
        self.connection.commit()
        id = self.cursor.lastrowid
        pessoa.id = id
        return pessoa.__dict__

    def update(self, pessoa:PessoaModel):
        self.cursor.execute(" UPDATE 01_MDG_PESSOA SET NOME = '{}', SOBRENOME = '{}', IDADE = {} WHERE ID = {}".format(pessoa.nome, pessoa.sobrenome, pessoa.idade, pessoa.id))
        self.connection.commit()
        return pessoa.__dict__

    def remove(self, id):
        self.cursor.execute("DELETE FROM 01_MDG_PESSOA WHERE ID = {}".format(id))
        self.connection.commit()
        return 'Removido a pessoa de id: {}'.format(id)
