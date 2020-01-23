import sys
sys.path.append('Aulas/Aula38')
from controller.squad_controller import SquadController


sc = SquadController()

for p in sc.listar_todos():
    print(p)