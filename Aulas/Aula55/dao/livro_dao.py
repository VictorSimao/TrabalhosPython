from Aulas.Aula55.dao.base_dao import BaseDao
from Aulas.Aula55.model.livro import Livro

class ClienteDao(BaseDao):
    def __init__(self):
        super().__init__(Livro)