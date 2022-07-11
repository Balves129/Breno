
from classe_lista import *
class Estoque:
    def __init__(self):
        self.puxar = []
        self.puxar.append(Produto(50,'carro','Mercedez',100))

    def cadastrar_produtos(self):
        entrada_cod = int(input('informe o codigo:\n'))
        entrada_nome = input('informe a descricao:\n')
        entrada_fab = input('informe Fabricante:\n')
        entrada_quant = int(input('informe a quantidade:\n'))
        self.puxar.append(Produto(cod=entrada_cod, nome=entrada_nome, fab=entrada_fab, quant=entrada_quant))
        print('produto salvo')

    def listar_produtos(self):
        for i in range(len(self.puxar)):
            print('cod:', self.puxar[i].cod, 'Nome:', self.puxar[i].nome, 'fab:', self.puxar[i].fab, 'quant',
                  self.puxar[i].quant)
            print('===================================================')

   
    def alterar_produto(self):
        entrada=input('Digite o código: ')
        for i in range(len(self.puxar)):
            if entrada == self.puxar[i].cod:
                self.puxar[i].nome= input('Nome do Produto: ')
                print('===============================================')
    
    
                       