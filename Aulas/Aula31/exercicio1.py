import MySQLdb
print('-'*50)
conexao = MySQLdb.connect(host='localhost',database='aula_bd',user='root',passwd='')
cursor = conexao.cursos()
cursor.execute('SELECT * FROM tb_pessoa')
pessoas = cursor.fetchall()
for p in pessoas:
    print(p)

print('-'*50)