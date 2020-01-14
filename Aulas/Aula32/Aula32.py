import MySQLdb

# listar todas as pessoas
def listar_todos(c):
    c.execute('SELECT * FROM PESSOA')
    pessoas = c.fetchall()
    for p  in  pessoas:
        print(p)

#buscar uma pessoa pelo ID
def buscar_por_id(c, IDPESSOA):
    c.execute(f'SELECT * FROM PESSOA WHERE IDPESSOA = {IDPESSOA}')
    pessoa = c.fetchone()
    print(pessoa)

#buscar pessoas por sobrenome
def buscar_por_sobrenome(c, SOBRENOME):
    c.execute(f"SELECT * FROM PESSOA WHERE SOBRENOME like '{SOBRENOME}%' ")
    for p  in  c.fetchall():
        print(p)


# conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019' )
conexao = MySQLdb.connect(host='localhost',database='aulabd',user='root',passwd='')
cursor= conexao.cursor()

#listar_todos(cursor)
# buscar_por_id(cursor, 3)
# buscar_por_sobrenome(cursor,'Gru')

#salvar pessoa
def salvar(cn, cr, NOME, SOBRENOME, IDADE, ENDERECO_ID='NULL'):
    # if endereco_id == None:
    #    endereco_id = 'NULL'
    cr.execute(f"INSERT INTO PESSOA (NOME, SOBRENOME, IDADE, ENDERECO_ID )VALUES('{NOME}', '{SOBRENOME}', {IDADE}, {ENDERECO_ID})")
    cn.commit()

#alterar pessoa
def alterar(cn, cr, IDPESSOA, NOME, SOBRENOME, IDADE, ENDERECO_ID='NULL'):
    cr.execute(f"UPDATE PESSOA SET NOME ='{NOME}', SOBRENOME='{SOBRENOME}', IDADE={IDADE}, ENDERECO_ID={ENDERECO_ID} WHERE IDPESSOA={IDPESSOA} ")
    cn.commit()

#deletar pessoa
def deletar(cn, cr, IDPESSOA):
    cr.execute(f'DELETE FROM PESSOA WHERE IDPESSOA={IDPESSOA}')
    cn.commit()

# listar_todos(cursor)
# buscar_por_id(cursor, 3)
# buscar_por_sobrenome(cursor,'Beltrano')
# salvar(conexao, cursor, 'Fulano', 'Beltrano', 28)
# alterar(conexao, cursor, 2, 'Fulano', 'Ciclano', 22)
# deletar(conexao, cursor, 4)

def salvar_end(cn, cr, LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO, CIDADE, CEP):
    cr.execute(f"INSERT INTO ENDERECO (LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO, CIDADE, CEP )VALUES('{LOGRADOURO}', '{NUMERO}', '{COMPLEMENTO}', '{BAIRRO}', '{CIDADE}', '{CEP}')")
    cn.commit()

def deletar_end(cn, cr, idENDERECO):
    cr.execute(f'DELETE FROM ENDERECO WHERE idENDERECO={idENDERECO}')
    cn.commit()

# salvar_end(conexao, cursor, 'Rua 25 de Dezembro', '225', None, 'Itoupava Norte', 'Blumenau', '89000-000')
# deletar_end(conexao, cursor, 3)
