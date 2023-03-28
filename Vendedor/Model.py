from TOCOMFOME import *



# Classe Vendedor:

class VENDEDOR(Base):
    __tablename__ = 'VENDEDOR'
    id = Column('CPF', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME',String(255), nullable=False)
    usuario = Column('USUARIO', String(50), nullable=False)
    telefone = Column('TELEFONE', String(15), nullable=False)
    email = Column('EMAIL',String(100), nullable=False)
    data_nasc = Column('DATA_NASC', Date, nullable=False)
    idLoja = Column('ID_LOJA', Integer, nullable=False)


    def __init__(self, nome, usuario, telefone, email, data_nasc):
        self.nome = nome
        self.usuario = usuario
        self.telefone = telefone
        self.email = email
        self.data_nasc = data_nasc



# Model da classe Cliente:


class Model_Vendedor():

    def visualizar_vendedores():
        sql = '''SELECT * FROM VENDEDOR'''
        vendedor = []
        v = {}
        result = consultar_db(sql)
        for l in result:
            v = {"id": l[0], "nome": l[1], "usuario": l[2], "email": l[3], "data_nasc": l[4] }
            vendedor.append(v)
        return vendedor

    def visualizar_vendedor(id_vendedor):
        sql = '''SELECT * FROM VENDEDOR'''
        vendedor = []
        v = {}
        result = consultar_db(sql)
        for l in result:
            v = {"id": l[0], "nome": l[1], "usuario": l[2], "email": l[3], "data_nasc": l[4] }
            vendedor.append(v)
        cont = 0
        for v in vendedor:
            if v['id'] == id_vendedor:
                return v
            elif v['id'] != id_vendedor:
                cont = cont + 1
            if cont == len(vendedor):
                return 'Esse id não pertence a lista de vendedores!'

    def adicionar_vendedor(nome, usuario, telefone, email, data_nasc):
        sql  = '''
        INSERT into vendedor(nome, usuario, telefone, email, data_nasc)
        values( '{}', '{}', '{}', '{}', '{}');
        '''.format(nome, usuario, telefone, email, data_nasc)
        inserir_db(sql)
        return 'Vendedor adicionado a lista com sucesso!'

    def excluir_vendedor(id_vendedor):
        sql = '''SELECT * FROM VENDEDOR;'''
        vendedor = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "nome": l[1], "usuario": l[2], "email": l[3], "data_nasc": l[4] }
            vendedor.append(i)
        id_vendedor = int(id_vendedor)
        cont = 0
        for i in vendedor:
            if i['id'] == id_vendedor:
                sql = '''
                Delete from vendedor where cpf = {};
                '''.format(id_vendedor)
                inserir_db(sql)
                return 'Vendedor excluido com sucesso!'
            elif i['id'] != id_vendedor:
                cont = cont + 1
            if cont == len(vendedor):
                return 'Esse id não pertence a lista de vendedores!'

    def atualizar_vendedor(id_vendedor, usuario, telefone, email):
        sql = '''
        UPDATE vendedor SET usuario='{}', telefone='{}', email='{}'
        WHERE cpf={};
        '''.format(usuario, telefone, email, id_vendedor)
        inserir_db(sql)
        return 'Atualizado com sucesso!'