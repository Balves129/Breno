from classe_trabalho import *

class Venda:
    def __init__(self):
        self.entrada = Estoque()
        self.saida_his= []    
    def vender(self):
        controle=int(input('Informe o código do produto: '))
        
        for i in range(len(self.entrada.puxar)):
            if controle == int(self.entrada.puxar[i].cod):
                his_venda=int(input('Informe a quantidade vendida: '))
                self.entrada.puxar[i].quant -= his_venda
                self.saida_his.append(f'Codigo do produto:{self.entrada.puxar[i].cod}/ Quantidade: {his_venda}')
            
                print('=======================================')
                print('Produto vendido! Atualizado com sucesso')
                print('=======================================')
            else:
                pass
        
        
    def venda_his(self):
        for i in range(len(self.saida_his)):
            print(self.saida_his[i])