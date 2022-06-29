from class_trabalho import *

class compra:
    def __init__(self):
        self.entrada = Estoque()
    
    def comprar(self):
        controle=int(input('Informe o código do produto: '))
        
        for i in range(len(self.entrada.listaProdutos)):
            if controle == self.entrada.listaProdutos[i].cod:
                self.entrada.listaProdutos[i].quantidade += \
                    int(input('Informe a quantidade comprada'))
            
            else:
                pass