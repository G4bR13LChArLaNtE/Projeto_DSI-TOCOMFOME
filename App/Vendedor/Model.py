from App.db import *


# Classe Vendedor:

class VENDEDOR(Base):
    __tablename__ = 'VENDEDOR'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    cpf = Column('CPF', Integer, nullable=False)
    nome = Column('NOME',String(255), nullable=False)
    usuario = Column('USUARIO', String(50), nullable=False)
    endereco = Column('ENDRECO', String(255), nullable=False)
    telefone = Column('TELEFONE', String(15), nullable=False)
    email = Column('EMAIL',String(100), nullable=False)
    data_nasc = Column('DATA_NASC', Date, nullable=False)
    id_loja = Column('ID_LOJA', Integer, nullable=False)


    def __init__(self, cpf, nome, usuario, telefone, email, data_nasc, id_loja):
        self.cpf = cpf
        self.nome = nome
        self.usuario = usuario
        self.telefone = telefone
        self.email = email
        self.data_nasc = data_nasc
        self.id_loja = id_loja



# Model da classe Vendedor:


class Model_Vendedor():

    def visualizar_vendedores():
        sql = '''SELECT * FROM VENDEDOR'''
        vendedor = []
        v = {}
        result = consultar_db(sql)
        for l in result:
            v = {"id": l[0], "cpf": l[1], "nome": l[2], "usuario": l[3], "telefone": l[4], "email": l[5], "data_nasc": l[6], "id_loja": l[7] }
            vendedor.append(v)
        if len(vendedor) == 0:
            return "Não há vendedor cadastrado!"
        else:
            return vendedor

    def visualizar_vendedor(cpf_vendedor):
        sql = '''SELECT * FROM VENDEDOR'''
        vendedor = []
        v = {}
        result = consultar_db(sql)
        for l in result:
            v = {"id": l[0], "cpf": l[1], "nome": l[2], "usuario": l[3], "telefone": l[4], "email": l[5], "data_nasc": l[6], "id_loja": l[7] }
            vendedor.append(v)
        cont = 0
        for v in vendedor:
            if v['cpf'] == cpf_vendedor:
                return v
            elif v['cpf'] != cpf_vendedor:
                cont = cont + 1
            if cont == len(vendedor):
                return 'Esse id não pertence a lista de vendedores!'

    def adicionar_vendedor(cpf, nome, usuario, telefone, email, data_nasc, id_loja):
        sql  = '''
        INSERT into vendedor(cpf, nome, usuario, telefone, email, data_nasc, id_loja)
        values( ?, ?, ?, ?, ?, ?, ?);
        '''
        tupla = (cpf, nome, usuario, telefone, email, data_nasc, id_loja)
        inserir_db(sql, tupla)
        return 'Vendedor adicionado a lista com sucesso!'

    def excluir_vendedor(cpf_vendedor):
        sql = '''SELECT * FROM VENDEDOR;'''
        vendedor = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "cpf": l[1], "nome": l[2], "usuario": l[3], "telefone": l[4], "email": l[5], "data_nasc": l[6], "id_loja": l[7] }
            vendedor.append(i)
        cpf_vendedor = int(cpf_vendedor)
        cont = 0
        for i in vendedor:
            if i['cpf'] == cpf_vendedor:
                sql = '''
                Delete from vendedor where cpf = ?;
                '''
                inserir_db(sql, cpf_vendedor)
                return 'Vendedor excluido com sucesso!'
            elif i['cpf'] != cpf_vendedor:
                cont = cont + 1
            if cont == len(vendedor):
                return 'Esse cpf não pertence a lista de vendedores!'

    def atualizar_vendedorNome(cpf_vendedor, nome):
        sql = '''
        UPDATE vendedor SET nome=?
        WHERE cpf=?;
        '''
        tupla = (nome, cpf_vendedor)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

    def atualizar_vendedorUsuario(cpf_vendedor, usuario):
        sql = '''
        UPDATE vendedor SET usuario=?
        WHERE cpf=?;
        '''
        tupla = (usuario, cpf_vendedor)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

    def atualizar_vendedorTelefone(cpf_vendedor, telefone):
        sql = '''
        UPDATE vendedor SET Telefone=?
        WHERE cpf=?;
        '''
        tupla = (telefone, cpf_vendedor)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

    def atualizar_vendedorEmail(cpf_vendedor, email):
        sql = '''
        UPDATE vendedor SET email=?
        WHERE cpf=?;
        '''
        tupla = (email, cpf_vendedor)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

    def atualizar_vendedorData(cpf_vendedor, data_nasc):
        sql = '''
        UPDATE vendedor SET data_nasc=?
        WHERE cpf=?;
        '''
        tupla = (data_nasc, cpf_vendedor)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

def atualizar_vendedorLoja(cpf_vendedor, id_loja):
        sql = '''
        UPDATE vendedor SET id_loja=?
        WHERE cpf=?;
        '''
        tupla = (id_loja, cpf_vendedor)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'
