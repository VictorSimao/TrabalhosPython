import sys
sys.path.append('Aulas/Aula38')

from controller.squad_controller import SquadController
from controller.backend_controller import BackEndController
from controller.frontend_controller import FrontEndController
from controller.sgbd_controller import SgbdController

from model.squad import Squad


sc = SquadController()
bc = BackEndController()
fc = FrontEndController()
sgc = SgbdController()


# ----------- Salvar um novo Squad no banco
# p = Squad()
# p.nome = 'Teste-5'
# p.descricao = 'Test5'
# p.numpessoas = 15
# p.backend.append(1)
# p.backend.append(2)
# p.frontend.append(1)
# p.sgbd.append(1)
# sc.salvar(p)

# ----------- Lista todos squads
# for i in sc.listar_todos():
#     print(i)

# ----------- Alterar squad especifico
# p = Squad()
# p.id = 7
# p.nome = 'Vendas'
# p.descricao = 'App de vendas'
# p.numpessoas = 12
# p.backend.append(4)
# p.frontend.append(3)
# p.sgbd.append(3)
# sc.alterar(p)

# ---------- Deletar o Squad especifico
# sc.deletar(9)
# print('\n\n\n\n\n')

# for i in sc.listar_todos():
#     print(i)

# ----------- Listar todas Linguagens Back End
# for i in bc.listar_todos():
#     print(i)

# ----------- Listar todos Framewoek Front End
# for i in fc.listar_todos():
#     print(i)

# ----------- Lista todos SGBD
# for i in sgc.listar_todos():
#     print(i)