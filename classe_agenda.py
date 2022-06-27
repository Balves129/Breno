from classe_contato import *

class Agenda:
        def __init__(self):
            self.listaContato = []

        def salvar_contatos(self):
            entrada_cod = input('Informe o código: ')
            entrada_nome = input('Informe o nome: ')
            entrada_celular = input('Informe o celular: ')
            self.listaContato.append(Contato(entrada_cod, entrada_nome, entrada_celular))
            print('Contato salvo com sucesso!')

        def listar_todos_contatos(self):
            for i in range(len(self.listaContato)):
                        print('cod:',self.listaContato[i].cod,
                        'nome:',self.listaContato[i].nome,
                        'celular:',self.listaContato[i].celular)
    
        
        def alterar_celular(self):
            entrada = input('Informe o código do contato: ')
            for i in range(len(self.listaContato)):
                if entrada == self.listaContato[i].cod:
                    self.listaContato[i].telefone = input('Digite o número novo: ')
                    
                
                            
                    