from Aulas.Aula55.controller.base_controller import BaseController
from Aulas.Aula55.model.autor import AutorDao

class AutorController(BaseController):
    def __init__(self):
        dao = AutorDao()
        super().__init__()