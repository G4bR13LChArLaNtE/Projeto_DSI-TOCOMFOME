from App.db import *



# Classe Categoria:

class Categoria (Base):
    __tablename__ = 'CATEGORIA'
    id = Column('ID_CATEGORIA', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)

    def __init__(self, nome):
        self.nome = nome






# Model da classe Categoria:


class Model_Categoria():
    def visualizar_categorias():
        sql = '''SELECT * FROM CATEGORIA'''
        categorias = []
        c = {}
        result = consultar_db(sql)
        for l in result:
            c = {"id": l[0], "nome": l[1] }
            categorias.append(c)
        if len(categorias) == 0:
            return "Não há categoria cadastrada!"
        else:
            return categorias

    def visualizar_categoria(id_categoria):
        sql = '''SELECT * FROM CATEGORIA'''
        categoria = []
        c = {}
        result = consultar_db(sql)
        for l in result:
            c = {"id": l[0], "nome": l[1] }
            categoria.append(c)
        cont = 0
        for c in categoria:
            if c['id'] == id_categoria:
                if c != None:
                    return c
                else:
                    'Não há esse id na lista!'
            elif c['id'] != id_categoria:
                cont = cont + 1
            if cont == len(categoria):
                return 'Esse id não pertence a lista de categorias!'

    def adicionar_categoria(nome):
        sql  = '''
        INSERT into categoria(nome)
        values( ? );
        '''
        inserir_db(sql, nome)
        return 'Categoria adicionada a lista com sucesso!'

    def excluir_categoria(id_categoria):
        sql = '''SELECT * FROM CATEGORIA;'''
        categoria = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "nome": l[1] }
            categoria.append(i)
        id_categoria = int(id_categoria)
        cont = 0
        for i in categoria:
            if i['id'] == id_categoria:
                sql = '''
                Delete from categoria where id_categoria = ?;
                '''
                inserir_db(sql, id_categoria)
                return 'Categoria excluida com sucesso!'
            elif i['id'] != id_categoria:
                cont = cont + 1
            if cont == len(categoria):
                return 'Esse id não pertence a lista de categorias!'

    def atualizar_categoria(id_categoria, nome):
        sql = '''
        UPDATE categoria SET nome= ?
        WHERE id_categoria= ?;
        '''
        tupla = (nome, id_categoria)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'