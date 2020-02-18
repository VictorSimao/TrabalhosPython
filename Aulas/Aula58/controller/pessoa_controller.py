from flask import request
from Aulas.Aula58.controller.base_controller import BaseController
from Aulas.Aula58.dao.pessoa_dao import PessoaDao
from Aulas.Aula58.model.pessoa import Pessoa

class PessoaController(BaseController):
    def __init__(self):
        dao = PessoaDao()
        super().__init__(dao)