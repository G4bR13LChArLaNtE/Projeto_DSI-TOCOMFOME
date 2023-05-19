from App.db import *
from App.Pedido.Model import *


# Classe Transacoes:

class TRANSACAO(Base):
    __tablename__ = 'TRANSACAO'
    id = Column('ID_TRANSACAO', Integer, primary_key=True, autoincrement=True)
    id_pedido = Column('ID_PEDIDO', Integer, nullable=False)
    id_produto = Column('ID_PRODUTO', Integer, nullable=False)
    nome_produto = Column('ID_LOJA', String(255), nullable=False)
    valor_produto = Column('VALOR_PRODUTO', Float, nullable=False)

    def __init__(self, id_pedido, id_produto, nome_produto, valor_produto):
        self.id_pedido = id_pedido
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.valor_produto = valor_produto

# Model da classe Transacao:


class Model_Transacao():

    def visualizar_transacoes():
        sql = '''SELECT * FROM TRANSACAO'''
        itens = []
        i = {}
        result = consultar_db(sql),
        for l in result:
            i = {"id": l[0], "id_pedido": l[1], "id_produto": l[2], "nome_produto": l[3], "valor_produto": l[4] }
            itens.append(i)
        if len(itens) == 0:
            return "Não há transações realizadas!"
        else:
            return itens

    def visualizar_pedido(id_pedido):
        sql = '''SELECT * FROM TRANSACAO'''
        itens = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "id_pedido": l[1], "id_produto": l[2], "nome_produto": l[3], "valor_produto": l[4] }
            itens.append(i)
        cont = 0
        for i in itens:
            if i['id_pedido'] == id_pedido:
                return i
            elif i['id_pedido'] != id_pedido:
                cont = cont + 1
            if cont == len(itens):
                return 'Pedido invalido, por favor, verifique o número do seu pedido!'

    def adicionar_produto(id_pedido, id_produto, nome_produto, valor_produto):
        sql  = '''
        INSERT into transacao(id_pedido, id_produto, nome_produto, valor_produto)
        values( ?, ?, ?, ?);
        '''
        tupla = (id_pedido, id_produto, nome_produto, valor_produto)
        inserir_db(sql, tupla)
        return 'Pedido adicionado a lista com sucesso!'

    def excluir_pedido(id_pedido):
        sql = '''SELECT * FROM TRANSACAO;'''
        itens = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "id_pedido": l[1], "id_produto": l[2], "nome_produto": l[3], "valor_produto": l[4]}
            itens.append(i)
        id_pedido = int(id_pedido)
        cont = 0
        for i in itens:
            if i['id_pedido'] == id_pedido:
                sql = '''
                Delete from transacao where id_pedido = ?;
                '''
                inserir_db(sql, id_pedido)
                return 'Pedido excluido com sucesso!'
            elif i['id_pedido'] != id_pedido:
                cont = cont + 1
            if cont == len(itens):
                return 'Esse id não pertence a lista de pedidos!'

    def calcular_valores(id_pedido, desconto):
        sql = '''SELECT * FROM TRANSACAO;'''
        itens = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "id_pedido": l[1], "id_produto": l[2], "nome_produto": l[3], "valor_produto": l[4]}
            itens.append(i)
        valores = 0
        id_pedido = int(id_pedido)
        cont = 0
        for i in itens:
            if i['id_pedido'] == id_pedido:
                valores += int(i['valor_produto'])
            elif i['id_pedido'] != id_pedido:
                cont = cont + 1
            if cont == len(itens):
                return 'Esse id não pertence a lista de pedidos!'
        Model_Pedido.set_total(valores, desconto)
