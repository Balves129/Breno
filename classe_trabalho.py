from classe_lista import *
class Estoque:
    def __init__(self):
        self.puxar = []
        self.puxar.append(Produto(2,'banana','breno',21))

    def salvar_produtos(self):
        entrada_cod = input('informe o codigo:\n')
        entrada_desc = input('informe a descricao:\n')
        entrada_fab = input('informe Fabricante e data:\n')
        entrada_quant = int(input('informe a quantidade:\n'))
        self.puxar.append(Produto(cod=entrada_cod, desc=entrada_desc, fab=entrada_fab, quant=entrada_quant))
        print('produto salvo')

    def listar_produtos(self):
        for i in range(len(self.puxar)):
            print('cod:', self.puxar[i].cod, 'desc:', self.puxar[i].desc, 'fab:', self.puxar[i].fab, 'quant',
                  self.puxar[i].quant)

   
    def alterar_produto(self):
        entrada=input('Escreve aí: ')
        for i in range(len(self.puxar)):
            if entrada == self.puxar[i].cod:
                self.puxar[i].desc= input('Escreve dnovo: ')
                print('=====================================')        
   
                            
                    