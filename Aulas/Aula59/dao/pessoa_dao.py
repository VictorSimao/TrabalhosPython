from Aulas.Aula59.dao.base_dao import BaseDao
from Aulas.Aula59.model.pessoa import Pessoa

class PessoaDao(BaseDao):
    def __init__(self):
        super().__init__(Pessoa)