#Teste de estudo

# Exibi uma letra por vez
for i in 'Python':
    print(i)

print('=======================')
# Adiciona 0, 1, 2 em a, b ,c consecutivamente
a, b, c = range(3)
print(a)
print(b)
print(c)

print('=======================')
# Exibi um item de cada vez e a lugar que esta indexado
aaa = ['item1', 'item2', 'item3']
for a, b in enumerate(aaa):
    print(a)
    print(b)

print('=======================')
# Exibi quantos items tem na lista
print(len(aaa))

# Adiciona item na lista
aaa.append('item4')

# Exibi quantos items tem na lista
print(len(aaa))

# Adiciona item em lugar especifico
aaa.insert(0, 'item0')

print(aaa)

print('=======================')
