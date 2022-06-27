from classe_agenda import*

class Menu:
    def __init__(self):
        agenda= Agenda ()
        
        ##INICAR MENU
        while True:
            entrada = input('Informe a opção desejada:'
                            '\n1 - Novo contato'
                            '\n2 - Listar Contato'
                            '\n3 - Alterar celular'
                            '\n4 - Sair\n') 
            
            if entrada == '1':
                agenda.salvar_contatos()
            
            elif entrada == '2':
                agenda.listar_todos_contatos()
            
            elif entrada == '3':
                agenda.alterar_celular()
            
            elif entrada == '4':
                break
            else:
                print('opção errada!')
                
                