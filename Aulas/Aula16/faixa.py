

def criar_faixa(musica,album,artista):
    faixa = {'musica':musica,'album':album,'artista':artista}
    return faixa

def salvar_faixa(faixa):
    arquivo = open('faixas.txt','a')
    arquivo.write(f"{faixa['musica']};{faixa['album']};{faixa['artista']}\n")
    arquivo.close()
    return faixa

def ler_faixa():
    playlist = []
    arquivo = open('faixas.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        linha_lista = linha.split(';')
        faixa = criar_faixa(linha_lista[0],linha_lista[1],linha_lista[2])
        playlist.append(faixa)
    arquivo.close()
    return playlist


