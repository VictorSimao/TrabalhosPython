def posicao(lista):
  for linha in lista:
    for indice, objeto in enumerate(linha):
      print(f'############# Posição {indice} #################\n{objeto}')