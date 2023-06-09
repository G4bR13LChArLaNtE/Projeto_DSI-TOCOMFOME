from App.db import *



# Classe Estoque:

class ESTOQUE(Base):
    __tablename__ = 'ESTOQUE'
    id = Column('ID_ESTOQUE', Integer, primary_key=True, autoincrement=True)
    produto = Column('PRODUTO', Integer, nullable=False)
    qtdProduto = Column('QTD_PRODUTO', Integer, nullable=False)
    idLoja = Column('ID_LOJA', Integer, nullable=False)

    def __init__(self, produto, qtdProduto):
        produto = []
        self.produto = produto
        qtdProduto = []
        self.qtdProduto = qtdProduto


# Model da classe Estoque:


class Model_Estoque():

    def visualizar_itens():
        sql = '''SELECT * FROM ESTOQUE'''
        itens = []
        i = {}
        result = consultar_db(sql),
        for l in result:
            i = {"id": l[0], "produto": l[1], "qtdProduto": l[2], "idLoja": l[3] }
            itens.append(i)
        if len(itens) == 0:
            return "Não há item cadastrado!"
        else:
            return itens

    def visualizar_item(item_id):
        sql = '''SELECT * FROM ESTOQUE'''
        itens = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "produto": l[1], "qtdProduto": l[2], "idLoja": l[3] }
            itens.append(i)
        cont = 0
        for i in itens:
            if i['id'] == item_id:
                return i
            elif i['id'] != item_id:
                cont = cont + 1
            if cont == len(itens):
                return 'Esse id não pertence a lista de itens!'

    def adicionar_item(id_loja, produto, qtdProduto):
        sql  = '''
        INSERT into estoque(produto, qtdProduto)
        values( ?, ?) WHERE ID_LOJA = ?;
        '''
        tupla = (produto, qtdProduto, id_loja)
        inserir_db(sql, tupla)
        return 'Item adicionado a lista com sucesso!'

    def excluir_item(item_id):
        sql = '''SELECT * FROM ESTOQUE;'''
        itens = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "produto": l[1], "qtdProduto": l[2], "idLoja": l[3]}
            itens.append(i)
        item_id = int(item_id)
        cont = 0
        for i in itens:
            if i['id'] == item_id:
                sql = '''
                Delete from estoque where id = ?;
                '''
                inserir_db(sql, item_id)
                return 'Item excluido com sucesso!'
            elif i['id'] != item_id:
                cont = cont + 1
            if cont == len(itens):
                return 'Esse id não pertence a lista de itens!'

    def atualizar_item(item_id, produto, qtdProduto):
        sql = '''
        UPDATE estoque SET produto = ?, qtdProduto= ?
        WHERE id= ?;
        '''
        tupla = (produto, qtdProduto, item_id)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'