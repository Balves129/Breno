from classe_trabalho import *
from sus import *
from classe_venda import*
class Menu:
    def __init__(self):
        estoque = Estoque()
        compra = Compra()
        saida = Venda()
        saida.entrada = estoque
        compra.entrada= estoque



        while True:
            entrada = input('1-Cadastrar produto\n2-Listar\n3-comprar Produto:\n4-Alterar Descrição:'
                            '\n5-Vender produto:\n6-historico de venda:\n7-historico de compra:\n8-Sair')
                            
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
                saida.vender()
            
            elif entrada== '6':
                saida.venda_his()
            
            elif entrada== '7':
                compra.his()
            
            elif entrada == '8':
                break


        