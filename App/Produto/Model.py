from App.db import *




# Classe Produto:

class PRODUTO(Base):
    __tablename__ = 'PRODUTO'
    id = Column('ID_PRODUTO', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)
    descricao = Column('DESCRICAO', String(255), nullable=True)
    imagem = Column('IMAGEM', VARBINARY(max), nullable=False)
    qtdProduto = Column('QTD_PRODUTO', Integer, nullable=False)
    valor = Column('VALOR_PRODUTO', Float, nullable=False)
    id_categoria = Column('ID_CATEGORIA', Integer, nullable=False)
    id_loja = Column('ID_LOJA', Integer, nullable=False)


    def __init__(self, nome, descricao, imagem, qtdProduto, valor, id_categoria, id_loja):
        self.nome = nome
        self.descricao = descricao
        self.imagem = imagem
        self.qtdProduto = qtdProduto
        self.valor = valor
        self.id_categoria = id_categoria
        self.id_loja = id_loja




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
        if len(produtos) == 0:
            return "Não há produto cadastrado!"
        else:
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

    def adicionar_produto(nome, descricao, imagem, qtdProduto, valor, id_categoria, id_loja):
        sql  = '''
        INSERT into produto(nome, descricao, imagem, qtdProduto, valor, id_categoria, id_loja)
        values( ?, ?, ?, ?, ?, ?, ?);
        '''
        tupla = (nome, descricao, imagem, qtdProduto, valor, id_categoria, id_loja)
        inserir_db(sql, tupla)
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
                Delete from produto where id_produto = ?;
                '''
                inserir_db(sql, id_produto)
                return 'Produto excluido com sucesso!'
            elif i['id'] != id_produto:
                cont = cont + 1
            if cont == len(produto):
                return 'Esse id não pertence a lista de produtos!'

    def atualizar_produtoNome(id_produto, nome):
        sql = '''
        UPDATE produto SET nome=?
        WHERE id_produto=?;
        '''
        tupla = (nome, id_produto)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

    def atualizar_produtoDescricao(id_produto, descricao):
        sql = '''
        UPDATE produto SET descricao=?
        WHERE id_produto=?;
        '''
        tupla = (descricao, id_produto)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

    def atualizar_produtoImagem(id_produto, imagem):
        sql = '''
        UPDATE produto SET imagem=?
        WHERE id_produto=?;
        '''
        tupla = (imagem, id_produto)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

    def atualizar_produtoQtd(id_produto, qtdProduto):
        sql = '''
        UPDATE produto SET qtdProduto=?
        WHERE id_produto=?;
        '''
        tupla = (qtdProduto, id_produto)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

    def atualizar_produtoValor(id_produto, valor):
        sql = '''
        UPDATE produto SET valor=?
        WHERE id_produto=?;
        '''
        tupla = (valor, id_produto)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

    def atualizar_produtoCategoria(id_produto, id_categoria):
        sql = '''
        UPDATE produto SET id_categoria=?
        WHERE id_produto=?;
        '''
        tupla = (id_categoria, id_produto)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

    def atualizar_produtoLoja(id_produto, id_loja):
        sql = '''
        UPDATE produto SET id_loja=?
        WHERE id_produto=?;
        '''
        tupla = (id_loja, id_produto)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'
