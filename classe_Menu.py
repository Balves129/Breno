from classe_trabalho import *
from sus import *
class Menu:
    def __init__(self):
        estoque = Estoque()
        compra = Compra()
        compra.entrada= estoque



        while True:
            entrada = input('1-Cadastrar produto\n2-Listar\n3-comprar Produto:\n4-Alterar Descrição: \n5-Sair:\n')
            print(80*'\033[34m=', '\033[m')
            if entrada == '1':
                estoque.salvar_produtos()
            
            elif entrada == '2':
                estoque.listar_produtos()
            
            elif entrada == '3':
                compra.comprar()
            
            elif entrada == '4':
                estoque.alterar_produto()
            
            elif entrada =='5':
                break
                