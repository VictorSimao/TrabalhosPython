import sys
sys.path.append('/Users/900165/Documents/TrabalhosPython/Aulas/Aula33-2/Aula33-4/')
from controller.pessoa_controller import PessoaController

pc = PessoaController()

for p in pc.listar_todos():
    print(p)