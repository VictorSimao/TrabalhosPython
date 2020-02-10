from Aulas.Aula55.dao.base_dao import BaseDao
from Aulas.Aula55.model.cliente import Cliente

class ClienteDao(BaseDao):
    def __init__(self):
        super().__init__(Cliente)