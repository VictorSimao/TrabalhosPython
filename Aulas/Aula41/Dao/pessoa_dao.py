
class PessoaDao:
    def list_all(self):
        return 'Listando todos os dados da tabela'

    def get_by_id(self, id):
        return 'Listando o dado de id: {}'.format(id)

    def insert(self, pessoa):
        return 'Cadastrando uma pessoa'

    def update(self, pessoa):
        return 'Alterando uma pessoa'

    def delete(self, id):
        return 'Removendo a pessoa de id: {}'.format(id)
