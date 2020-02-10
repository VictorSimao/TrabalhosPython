from Aulas.Aula55.dao.base_dao import BaseDao
from Aulas.Aula55.model.editora import Editora

class EdiroraDao(BaseDao):
    def __init__(self):
        super().__init__(Editora)