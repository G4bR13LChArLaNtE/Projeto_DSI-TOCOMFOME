from Projeto_DSI import *




# Classe Produto:

class PRODUTO(Base):
    __tablename__ = 'PRODUTO'
    id = Column('IDPRODUTO', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)
    descricao = Column('DESCRICAO', String(255), nullable=True)
    imagem = Column('IMAGEM', String(255), nullable=False)
    qtdProduto = Column('QTDPRODUTO', Integer, nullable=False)
    valor = Column('VALOR', Double, nullable=False)
    id_categoria = Column('ID_CATEGORIA', Integer, nullable=False)
    id_loja = Column('ID_LOJA', Integer, nullable=False)


    def __init__(self, nome, descricao, imagem, qtdProduto, valor, id_categoria):
        self.nome = nome
        self.descricao = descricao
        self.imagem = imagem
        self.qtdProduto = qtdProduto
        self.valor = valor
        self.id_categoria = id_categoria



# Model da classe Produto:



class Model_Produto():

    def visualizar_produtos():
        sql = '''SELECT * FROM PRODUTO'''
        produtos = []
        p = {}
        result = consultar_db(sql)
        for l in result:
            p = {"id": l[0], "nome": l[1], "descricao": l[2], "imagem": l[3], "qtdProduto": l[4], "valor": l[5], "id_categoria": l[6]}
            produtos.append(p)
        return produtos

    def visualizar_produto(id_produto):
        sql = '''SELECT * FROM PRODUTO'''
        produto = []
        p = {}
        result = consultar_db(sql)
        for l in result:
            p = {"id": l[0], "nome": l[1], "descricao": l[2], "imagem": l[3], "qtdProduto": l[4], "valor": l[5], "id_categoria": l[6]}
            produto.append(p)
        cont = 0
        for p in produto:
            if p['id'] == id_produto:
                return p
            elif p['id'] != id_produto:
                cont = cont + 1
            if cont == len(produto):
                return 'Esse id não pertence a lista de produtos!'

    def adicionar_produto(nome, descricao, imagem, qtdProduto, valor, id_categoria):
        sql  = '''
        INSERT into produto(nome, descricao, imagem, qtdProduto, valor, id_categoria)
        values( '{}', '{}', '{}', '{}', '{}', '{}');
        '''.format(nome, descricao, imagem, qtdProduto, valor, id_categoria)
        inserir_db(sql)
        return 'Produto adicionado a lista com sucesso!'

    def excluir_produto(id_produto):
        sql = '''SELECT * FROM PRODUTO;'''
        produto = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "nome": l[1], "descricao": l[2], "imagem": l[3], "qtdProduto": l[4], "valor": l[5] }
            produto.append(i)
        id_produto = int(id_produto)
        cont = 0
        for i in produto:
            if i['id'] == id_produto:
                sql = '''
                Delete from produto where id = {};
                '''.format(id_produto)
                inserir_db(sql)
                return 'Produto excluido com sucesso!'
            elif i['id'] != id_produto:
                cont = cont + 1
            if cont == len(produto):
                return 'Esse id não pertence a lista de produtos!'

    def atualizar_produto(id_produto, nome, descricao, imagem, qtdProduto, valor, id_categoria):
        sql = '''
        UPDATE produto SET nome='{}', descricao='{}', imagem='{}', qtdProduto='{}', valor='{}', id_categoria='{}'
        WHERE id={};
        '''.format(nome, descricao, imagem, qtdProduto, valor, id_categoria, id_produto)
        inserir_db(sql)
        return 'Atualizado com sucesso!'