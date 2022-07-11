from classe_trabalho import *
from sus import *
from classe_venda import*
from classe_estoque import DB_estoque

class Menu:
    def __init__(self):
        estoque = DB_estoque()
        compra = Compra()
        saida = Venda()
        saida.entrada = estoque
        compra.entrada= estoque



        while True:
            entrada = input('1-Cadastrar produto\n2-Listar\n3-comprar Produto:\n4- listar fabricante:'
                            '\n5-Vender produto:\n6-historico de venda:\n7-historico de compra:\n0-Sair')
                            
            print(80*'\033[34m=', '\033[m')
            if entrada == '1':
                cod=int(input('Digite o codigo do produto: '))
                nome= (input("Cadastre seu produto: "))
                cod_fabricante = int(input('Digite o codigo do fabricante: '))
                quant = int(input('Digite a quantidade: '))
                estoque.cadastrar_produtos(cod, nome, cod_fabricante, quant)

            
            elif entrada == '2':
                estoque.listar_produtos()
            
            elif entrada == '3':
                compra.comprar()
            
            elif entrada == '4':
                estoque.listar_fab()
            
            elif entrada =='5':
                saida.vender()
            
            elif entrada== '6':
                saida.venda_his()
            
            elif entrada== '7':
                compra.his()
            
            elif entrada == '0':
                break


        