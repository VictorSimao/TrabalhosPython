# Cadastro de Banda, Album, Musica, Sair
# Ao sair, mostra bandas, albuns, musicas.


menu = '''
1 - Banda
2 - Album
3 - Musica
4 - Sair

Digite a opção: '''
bandas = []
albuns = []
musicas = []

while True:
    opcao = input(menu)
    if opcao == '1':
        bandas.append(input('Digite a banda: '))
    elif opcao == '2':
        albuns.append(input('Digite o album: '))
    elif opcao == '3':
        musicas.append(input('Digite a musica: '))
    elif opcao == '4':
        print(f'Bandas: {bandas}\nAlbuns: {albuns}\nMusicas: {musicas}')
        break
    else:
        print('Valor Invalido')


