from Projeto_DSI import *




# Classe Loja:

class Loja(Base):
    __tablename__ = 'LOJA'
    id = Column('ID_LOJA', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME',String(255), nullable=False)
    descricao = Column('DESCRICAO', String(255))
    logo = Column('LOGO', String(255))
    endereco = Column('ENDERECO', String(255))
    horario_func = Column('HORARIO_FUNC', Date, nullable=False)
    nota = Column('NOTA', Integer)
    id_vendedor = Column('ID_VENDEDOR', Integer, nullable=False)


    def __init__(self, nome, descricao, logo, endereco, horario_func, nota, id_vendedor):
        self.nome = nome
        self.descricao = descricao
        self.logo = logo
        self.endereco = endereco
        self.horario_func = horario_func
        self.nota = nota
        self.id_vendedor = id_vendedor


# Model da classe Cliente:


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
            sql = "SELECT * FROM VENDEDOR WHERE CPF = '{}'".format(id_vendedor)
            v = {}
            result = consultar_db(sql)
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
            sql = "SELECT * FROM VENDEDOR WHERE CPF = '{}'".format(id_vendedor)
            v = {}
            result = consultar_db(sql)
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
        values( '{}', '{}', '{}', '{}', '{}', '{}', '{}');
        '''.format(nome, descricao, logo, endereco, horario_func, nota, id_vendedor)
        inserir_db(sql)
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
                Delete from loja where id_loja = {};
                '''.format(id_loja)
                inserir_db(sql)
                return 'Loja excluido com sucesso!'
            elif i['id'] != id_loja:
                cont = cont + 1
            if cont == len(loja):
                return 'Esse id não pertence a lista de lojas!'

    def atualizar_vendedor(id_loja, nome, descricao, logo, endereco, horario_func):
        sql = '''
        UPDATE vendedor SET
        nome='{}', descricao='{}', logo='{}', endereco='{}', horario='{}'
        WHERE id_loja={};
        '''.format(nome, descricao, logo, endereco, horario_func, id_loja)
        inserir_db(sql)
        return 'Atualizado com sucesso!'
