import sys
sys.path.append('C:/Users/900165/Documents/TrabalhosPython/Aulas/Aula37')
from controller.squad_controller import SquadController


sc = SquadController()

for p in sc.listar_todos():
    print(p)