from classe_trabalho import *

class Compra:
    def __init__(self):
        self.entrada = Estoque()
    
    def comprar(self):
        controle=int(input('Informe o código do produto: '))
        
        for i in range(len(self.entrada.puxar)):
            if controle == self.entrada.puxar[i].cod:
                self.entrada.puxar[i].quant += \
                    int(input('Informe a quantidade comprada: '))
                print('=======================================')
                print('Produto comprado!')
            
            else:
                pass
            
            