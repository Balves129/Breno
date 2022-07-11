import mysql.connector
from classe_lista import Produto

#Create
class DB_estoque():
    def __init__(self):
        self.conexao = mysql.connector.connect( host='localhost',user= 'root',password= 'q1w2e3',database = 'Loja')
        self.mycursor = self.conexao.cursor()

    def cadastrar_produtos(self, cod, nome, cod_fabricante, quant):
        comandoSQL = 'select codigo from Fabricante'
        self.mycursor.execute(comandoSQL)
        ListaSQL= self.mycursor.fetchall()
        for i in ListaSQL:
            if int(cod_fabricante) == i[0]:

                obj_produto = Produto(cod, nome, cod_fabricante, quant)
                comando1 = f'insert into Produtos(cod, nome, cod_fabricante, quant) value("{obj_produto.cod}","{obj_produto.nome}","{obj_produto.cod_fabricante}","{obj_produto.quant}")'

                self.mycursor.execute(comando1)
                self.conexao.commit()

#Read
    def listar_produtos(self):
        comando1 = 'select * from Produtos'
        self.mycursor.execute(comando1)
        lista = self.mycursor.fetchall()
        for i in lista:
            print(i)

    #def listar_fab(self):
    #    comando1 = 'select * from Fabricante'
    #    self.cursor.execute(comando1)
    #    lista = self.cursor.fetchall()
    #    for i in lista:
    #        print(i)

