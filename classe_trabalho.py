from classe_lista import *
class Estoque:
    def __init__(self):
        self.puxar = []

    def salvar_produtos(self):
        entrada_cod = input('informe o codigo:\n')
        entrada_desc = input('informe a descricao:\n')
        entrada_fab = input('informe a fabricacao:\n')
        entrada_quant = input('informe a quantidade:\n')
        self.puxar.append(Produto(cod=entrada_cod, desc=entrada_desc, fab=entrada_fab, quant=entrada_quant))
        print('produto salvo')

    def listar_produtos(self):
        for i in range(len(self.puxar)):
            print('cod:', self.puxar[i].cod, 'desc:', self.puxar[i].desc, 'fab:', self.puxar[i].fab, 'quant',
                  self.puxar[i].quant)

    def trocar_produto(self):
        coloca = input('informe o codigo do produto:\n')
        for i in range(len(self.puxar)):
            if coloca == self.puxar[i].cod:
                self.puxar[i].Produto = input('digite o codigo novo:\n')

   
                            
                    