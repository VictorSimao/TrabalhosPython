from Aulas.Aula60.ForTwo.r2.local import Local

class Aviao(Local):
    def __init__(self):
        self.__pessoas = []
        super().__init__(self.__pessoas)

    def __str__(self):
        return 'Avião'