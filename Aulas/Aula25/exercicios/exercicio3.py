# Aula 25 - 12-12-2019


# Produto

# Crie uma classe produto.

# Esta classe deve ter como atributo: codigo produto(int), nome, marca, preço de custo(float),
# preço de venda(float) e quantidade em estoque(int).

# Cada produto deve ter um código unico e sequencial.
# Só pode vender produtos que tenha no estoque.

# Metodos: Atualizar dados do produto, adicionar e 
# remover produtos do estoque, __str__ e __eq__ (para pesquisar mais facilmente o
# código do produto)


class Produto:
    def __init__(self,codigo, nome, marca, preco_custo, preco_venda, estoque):
        self.lista_produto = []
        self.codigo = codigo
        self.nome = nome
        self.marca = marca
        self.preco_custo = preco_custo
        self.preco_venda = preco_venda
        self.estoque = estoque
        
    
    def ver_produtos(self,lista_produto):
        for linha in lista_produto:
            print(f'Codigo: {self.codigo}')
            print(f'Nome: {self.nome}')
            print(f'Marca: {self.marca}')
            print(f'Preço de custo: {self.preco_custo}')
            print(f'Preço de venda: {self.preco_venda}')
            print(f'Estoque: {self.estoque}')


    def atualizar (self):
        '''
        Este metodo serve para atualizar o cadastro do produto. 
        Os dados que podem ser atualizados são: 
        nome, marca, preço de custo(float),preço de venda(float)
        '''
        pass

    def atualizar_estoque(self):
        '''
        Esta função é usada para atualizar a quantidade de produto no estoque.
        
        '''
        pass

    

    def __eq__(self,valor):
        '''
        Este metodo deve comparar se o valor do código é igual ao valor.
        Se positivo ele retorna True caso contrário retorna False
        '''
        pass

    def __srt__(self):
        '''
        Este metodo deve retornar uma string com todos os dados.
        Use f-string para interpolar o texto com as variáveis
        '''
        pass

lista_produto = []
while True:
    codigo = len(lista_produto)
    nome = input('Nome: ')
    marca = input('Marca: ')
    preco_custo = float(input('Preço de custo: '))
    preco_venda = float(input('Preço de venda: '))
    estoque = int(input('Estoque: '))

    p = Produto(codigo,nome,marca,preco_custo,preco_venda,estoque)
    lista_produto.append(p)
    p.ver_produtos()
