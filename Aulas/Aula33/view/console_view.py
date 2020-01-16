import sys
sys.path.append('C:/Users/900165/Documents/TrabalhosPython/Aulas/Aula33')
from controller.pessoa_controller import PessoaController
from controller.endereco_controller import EnderecoController

ec = EnderecoController()
pc = PessoaController()

for p in pc.listar_todos():
    print(p)

for p in ec.listar_todos():
    print(p)