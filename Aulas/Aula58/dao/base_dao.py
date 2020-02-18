
class BaseDao:
    def __init__(self):
        self.lista_pessoas = []
        arquivo = open("C:/Users/900161/Documents/TrabalhosPython/exercicio_api/pessoas.txt", "r")
        for pessoas in arquivo:
            pessoas = pessoas.strip()
            self.lista_pessoas.append(pessoas)

    def list_all(self):
        return self.lista_pessoas

    def get_by_id(self, id):
        for i in self.lista_pessoas:
            for j in i:
                if id in j:
                    return print(i)

    def insert(self):
        retorno = 'S'
        arquivo = open("C:/Users/900161/Documents/TrabalhosPython/exercicio_api/pessoas.txt", "a")
        while retorno == 'S':
            retorno = input('Gostaria de adicionar alguém a lista? (S/N) ')
            retorno.upper()
            if retorno == 'S':
                arquivo.write('\n'+input('Digite o nome da pessoa a ser adicionada: '))
            arquivo.close()
        return f"objeto(s) inserido(s) com sucesso!"

    def delete(self, id):
        arquivo = open("C:/Users/900161/Documents/TrabalhosPython/exercicio_api/pessoas.txt", "w")
        for i in arquivo:
            if i == id:
                self.lista_pessoas.remove(id)
        return f"objeto deletado com sucesso!"