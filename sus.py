from classe_trabalho import *

class Compra:
    def __init__(self):
        self.entrada = Estoque()
        self.historico = []
    def comprar(self):
        controle=int(input('Informe o código do produto: '))
        
        for i in range(len(self.entrada.puxar)):
            if controle == int(self.entrada.puxar[i].cod):
                histo=int(input('informe quantidade comprada: '))
                self.entrada.puxar[i].quant += histo
                self.historico.append(f'Código do produto: {self.entrada.puxar[i].cod}/ Quantidade: {histo}')
                print('=======================================')
                print('Finalizado!')
                print('=======================================')
            else:
                pass
    
    def his(self):
        for i in range(len(self.historico)):
             print(self.historico[i])
             