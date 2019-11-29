# Aula 16 - 29-11-2019
# Cadastro musica, artista, album

from faixa import criar_faixa, salvar_faixa, ler_faixa

musica = input('Musica: ')
artista = input('Artista: ')
album = input('Album: ')

faixa = criar_faixa(musica,album,artista)
playlist = salvar_faixa(faixa)

for linha in ler_faixa():
    print(f"Musica:{linha['musica']} Album:{linha['album']} Artista:{linha['artista']}")

