#----- Importar biblioteca do Mysql
import MySQLdb
from model.endereco import Endereco

class EnderecoDb:
    #----- Configurar a conexão
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
    #----- Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()
    
    def listar_todos(self):
        #----- Criação do comando SQL e passado para o cursor
        comando_sql_select = "SELECT * FROM ENDERECO"
        self.cursor.execute(comando_sql_select)
        #---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
        resultado = self.cursor.fetchall()
        lista_endereco_classe = self.converter_tabela_classe(resultado)
        return lista_endereco_classe

    def buscar_por_id(self, id):
        #----- Criação do comando SQL e passado para o cursor
        comando_sql_select = f"SELECT * FROM ENDERECO WHERE IDENDERECO= {id}"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone()
        return resultado

    def converter_tabela_classe(self, lista_tuplas):
        #cria uma lista para armazenar os dicionarios
        lista_endereco = []
        for p in lista_tuplas:
            #----- Criação do objeto da classe pessoa
            p1 = Endereco()
            #--- pega cada posição da tupla e atribui a uma chave do dicionário
            p1.id = p[0]
            p1.logradouro = p[1]
            p1.numero= p[2]
            p1.complemento = p[3]
            p1.bairro = p[4]
            p1.cidade=p[5]
            p1.cep=p[6]
            lista_endereco.append(p1)
        return lista_endereco