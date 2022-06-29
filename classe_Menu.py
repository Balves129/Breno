from classe_trabalho import *
class Menu:
    def __init__(self):
        estoque = Estoque()
        



        while True:
            entrada = input('1-Cadastrar\n2-Listar\n3-Trocar Produto:\n''4-Sair:\n')
            print(80*'\033[34m=', '\033[m')
            if entrada == '1':
                estoque.salvar_produtos()
            elif entrada == '2':
                estoque.listar_produtos()
            elif entrada == '3':
                estoque.trocar_produto()
            elif entrada == '4':
                break
                