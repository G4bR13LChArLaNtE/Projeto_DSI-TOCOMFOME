from App.db import *




# Classe Loja:

class Loja(Base):
    __tablename__ = 'LOJA'
    id = Column('ID_LOJA', Integer, primary_key=True, autoincrement=True)
    id_vendedor = Column('CPF_VENDEDOR', Integer, nullable=False)
    nome = Column('NOME_LOJA',String(255), nullable=False)
    descricao = Column('DESCRICAO', String(500))
    logo = Column('LOGO', VARBINARY(max))
    endereco = Column('ENDERECO', String(255))
    horario_func = Column('HORARIO_FUNC', String(10), nullable=False)
    nota = Column('NOTA', Integer)
    


    def __init__(self, nome, descricao, logo, endereco, horario_func, nota, id_vendedor):
        self.nome = nome
        self.descricao = descricao
        self.logo = logo
        self.endereco = endereco
        self.horario_func = horario_func
        self.nota = nota
        self.id_vendedor = id_vendedor


# Model da classe Loja:


class Model_Loja():

    def visualizar_lojas():
        sql = '''SELECT * FROM LOJA'''
        lojas = []
        l = {}
        result = consultar_db(sql)
        id_vendedor = ""
        for i in result:
            l = {"id": i[0], "nome": i[1], "descricao": i[2], "logo": i[3], "endereco": i[4],"horario_func": i[5], "nota": i[6]}
            lojas.append(l)
            id_vendedor = i[7]
            sql = "SELECT * FROM VENDEDOR WHERE CPF_VENDEDOR = ?"
            v = {}
            result = consultar_db(sql, id_vendedor)
            for i in result:
                v = {"nome_vendedor" : i[1], "Apelido_vendedor": i[2]}
                lojas.update(v)
        return lojas

    def visualizar_loja(id_loja):
        sql = '''SELECT * FROM LOJA'''
        loja = []
        l = {}
        result = consultar_db(sql)
        for i in result:
            l = {"id": i[0], "nome": i[1], "descricao": i[2], "logo": i[3], "endereco": i[4],"horario_func": i[5], "nota": i[6] }
            loja.append(l)
            id_vendedor = i[7]
            id_vendedor = int(id_vendedor)
            sql = "SELECT * FROM VENDEDOR WHERE CPF = ?"
            v = {}
            result = consultar_db(sql, id_vendedor)
            for i in result:
                v = {"nome_vendedor" : i[1], "Apelido_vendedor": i[2]}
                loja.update(v)
        cont = 0
        for l in loja:
            if l['id'] == id_loja:
                return l
            elif l['id'] != id_loja:
                cont = cont + 1
            if cont == len(loja):
                return 'Esse id não pertence a lista de lojas!'

    def adicionar_loja(nome, descricao, logo, endereco, horario_func, nota, id_vendedor):
        sql  = '''
        INSERT into loja(nome, descricao, logo, endereco, horario_func, nota, id_vendedor)
        values( ?, ?, ?, ?, ?, ?, ?);
        '''
        tupla = (nome, descricao, logo, endereco, horario_func, nota, id_vendedor)
        inserir_db(sql, tupla)
        return 'Loja adicionadoa a lista com sucesso!'

    def excluir_loja(id_loja):
        sql = '''SELECT * FROM LOJA;'''
        loja = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "nome": l[1], "descricao": l[2], "logo": l[3], "endereco": l[4],"horario_func": l[5], "nota": l[6] }
            loja.append(i)
        id_loja = int(id_loja)
        cont = 0
        for i in loja:
            if i['id'] == id_loja:
                sql = '''
                Delete from loja where id_loja = ?;
                '''
                inserir_db(sql, id_loja)
                return 'Loja excluido com sucesso!'
            elif i['id'] != id_loja:
                cont = cont + 1
            if cont == len(loja):
                return 'Esse id não pertence a lista de lojas!'

    def atualizar_nome(id_loja, nome):
        sql = '''
        UPDATE loja SET
        nome=?
        WHERE id_loja=?;
        '''
        tupla = (nome, id_loja)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

    def atualizar_nome(id_loja, nome):
        sql = '''
        UPDATE loja SET
        nome=?
        WHERE id_loja=?;
        '''
        tupla = (nome, id_loja)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

    def atualizar_descricao(id_loja, descricao):
        sql = '''
        UPDATE loja SET
        descricao=?
        WHERE id_loja=?;
        '''
        tupla = (descricao, id_loja)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

    def atualizar_logo(id_loja, logo):
        sql = '''
        UPDATE loja SET
        logo=?
        WHERE id_loja=?;
        '''
        tupla = (logo, id_loja)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

    def atualizar_endereco(id_loja, endereco):
        sql = '''
        UPDATE loja SET
        endereco=?
        WHERE id_loja=?;
        '''
        tupla = (endereco, id_loja)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

    def atualizar_horario(id_loja, horario):
        sql = '''
        UPDATE loja SET
        horario_func=?
        WHERE id_loja=?;
        '''
        tupla = (horario, id_loja)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'


