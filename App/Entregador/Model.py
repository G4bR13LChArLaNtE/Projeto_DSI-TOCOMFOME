from App.db import *
from App import Pedido


# Classe Entregador:

class ENTREGADOR(Base):
    __tablename__ = 'ENTREGADOR'
    id = Column('ID_ENTREGADOR', Integer, primary_key=True, autoincrement=True)
    cpf_entregador = Column('CPF_ENTREGADOR', Integer, nullable=False)
    nome = Column('NOME',String(255), nullable=False)
    telefone = Column('TELEFONE', String(15), nullable=False)


    def __init__(self, cpf_entregador, nome, telefone):
        self.cpf_entregador = cpf_entregador
        self.nome = nome
        self.telefone = telefone


# Model da classe Entregador:

class Model_Entregador():
    def visualizar_entregadores():
        sql = '''SELECT * FROM ENTREGADOR'''
        entregadores = []
        e = {}
        result = consultar_db(sql)
        for l in result:
            e = {"id": l[0], "nome": l[2], "Telefone":l[3] }
            entregadores.append(e)
        if len(entregadores) == 0:
            return "Não há entregador cadastrado!"
        else:
            return entregadores

    def visualizar_entregador(id_entregador):
        sql = '''SELECT * FROM ENTREGADOR'''
        entregador = []
        e = {}
        result = consultar_db(sql)
        for l in result:
            e = {"id": l[0], "nome": l[2], "Telefone":l[3] }
            entregador.append(e)
        cont = 0
        for e in entregador:
            if e['id'] == id_entregador:
                if e != None:
                    return e
                else:
                    'Não há esse id na lista!'
            elif e['id'] != id_entregador:
                cont = cont + 1
            if cont == len(entregador):
                return 'Esse id não pertence a lista de entregadores!'

    def adicionar_entregador(cpf, nome, telefone):
        sql  = '''
        INSERT into entregador(cpf, nome, telefone)
        values( ?, ?, ? );
        '''
        tupla = (cpf, nome, telefone)
        inserir_db(sql, tupla)
        return 'Entregador adicionado a lista com sucesso!'

    def excluir_entregador(id_entregador):
        sql = '''SELECT * FROM ENTREGADOR;'''
        entregador = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "nome": l[1] }
            entregador.append(i)
        id_entregador = int(id_entregador)
        cont = 0
        for i in entregador:
            if i['id'] == id_entregador:
                sql = '''
                Delete from entregador where id_entregador = ?;
                '''
                inserir_db(sql, id_entregador)
                return 'Entregador excluido com sucesso!'
            elif i['id'] != id_entregador:
                cont = cont + 1
            if cont == len(entregador):
                return 'Esse id não pertence a lista de entregadores!'

    def atualizar_entregador_nome(id_entregador, nome):
        sql = '''
        UPDATE entregador SET nome= ?
        WHERE id_entregador= ?;
        '''
        tupla = (nome, id_entregador)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

    def atualizar_entregador_cpf(id_entregador, cpf):
        sql = '''
        UPDATE entregador SET cpf_entregador= ?
        WHERE id_entregador= ?;
        '''
        tupla = (cpf, id_entregador)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'
