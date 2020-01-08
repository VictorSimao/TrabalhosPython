class airlines:
    '''
    Classe que possibilita listar as pessoas em cada
    lugar (carro, avião e terminal) e transferi-los.
    '''
    def listar_terminal(self, terminal):
        '''
        Lista todas as pessoas que estão no terminal.
        '''
        for i in range(len(terminal)):
            print(terminal[i])

    def listar_aviao(self, aviao):
        '''
        Lista todas as pessoas que estão no avião.
        '''
        for pessoa in aviao:
            print(pessoa)

    def listar_carro(self, carro):
        '''
        Lista todas as pessoas que estão no carro.
        '''
        if not carro:
            print('\nCarro: Vazio')
        else:
            try:
                print(f'\nCarro: {carro[0]} e {carro[1]}')
            except IndexError:
                print(f'\nCarro: {carro[0]}')

    def transfer(self, recebe, exclue):
        '''
        Realiza a tranferência dos passageiros.
        '''
        recebe.append(exclue[0])
        exclue.pop(0)
    
    def abrir(self):
        arquivo = open('Aulas/Aula29/pessoas.txt', 'r')
        lista = []
        for pessoa in arquivo:
            pessoa = pessoa.strip()
            lista.append(pessoa)
        arquivo.close()
        return lista

    def gravar(self, aviao):
        arquivo = open('Aulas/Aula29/aviao.txt', 'w')
        for pessoa in aviao:
            arquivo.write(f'{pessoa}\n')
        arquivo.close()