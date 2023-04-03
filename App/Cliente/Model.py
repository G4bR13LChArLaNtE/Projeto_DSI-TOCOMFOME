from App.db import *



# Classe Cliente:

class CLIENTE(Base):
    __tablename__ = 'CLIENTE'
    id = Column('CPF', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME',String(255), nullable=False)
    usuario = Column('USUARIO', String(50), nullable=False)
    endereco = Column('ENDERECO', String(255), nullable=False)
    telefone = Column('TELEFONE', String(15), nullable=False)
    email = Column('EMAIL',String(100), nullable=False)
    data_nasc = Column('DATA_NASC', String(100), nullable=False)


    def __init__(self, nome, usuario, endereco, telefone, email, data_nasc):
        self.nome = nome
        self.usuario = usuario
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.data_nasc = data_nasc


# Model da classe Cliente:


class Model_Cliente():

    def visualizar_clientes():
        sql = '''SELECT * FROM CLIENTE'''
        clientes = []
        c = {}
        result = consultar_db(sql)
        for l in result:
            c = {"id": l[0], "nome": l[1], "usuario": l[2], "endereco": l[3], "email": l[4], "data_nasc": l[5] }
            clientes.append(c)
        if len(clientes) == 0:
            return "Não há clientes ainda na lista."
        else:
            return clientes

    def visualizar_cliente(id_cliente):
        sql = '''SELECT * FROM CLIENTE'''
        cliente = []
        c = {}
        result = consultar_db(sql)
        for l in result:
            c = {"id": l[0], "nome": l[1], "usuario": l[2], "endereco": l[3], "email": l[4], "data_nasc": l[5] }
            cliente.append(c)
        cont = 0
        for c in cliente:
            if c['id'] == id_cliente:
                return c
            elif c['id'] != id_cliente:
                cont = cont + 1
            if cont == len(cliente):
                return 'Esse id não pertence a lista de vendedores!'

    def adicionar_cliente(nome, usuario, endereco, telefone, email, data_nasc):
        sql  = '''
        INSERT into CLIENTE(nome, usuario, endereco, telefone, email, data_nasc)
        values( ?, ?, ?, ?, ?, ?);
        '''
        tupla = (nome, usuario, endereco, telefone, email, data_nasc)
        inserir_db(sql, tupla )
        return 'Cliente adicionado a lista com sucesso!'

    def excluir_cliente(id_cliente):
        sql = '''SELECT * FROM CLIENTE;'''
        cliente = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "nome": l[1], "usuario": l[2], "email": l[3], "data_nasc": l[4] }
            cliente.append(i)
        id_cliente = int(id_cliente)
        cont = 0
        for i in cliente:
            if i['id'] == id_cliente:
                sql = '''
                Delete from cliente where cpf = ?;
                '''
                inserir_db(sql, id_cliente)
                return 'Cliente excluido com sucesso!'
            elif i['id'] != id_cliente:
                cont = cont + 1
            if cont == len(cliente):
                return 'Esse id não pertence a lista de clientes!'

    def atualizar_cliente(id_cliente, usuario, endereco, telefone, email):
        sql = '''
        UPDATE cliente SET usuario=?, endereco=?, telefone=?, email=?
        WHERE cpf=?;
        '''
        tupla = (usuario, endereco, telefone, email, id_cliente)
        inserir_db(sql, tupla)
        return 'Atualizado com sucesso!'

    def adicionar_nota(id_loja, nota):
        novaNota = 0
        sql = '''SELECT * FROM LOJA'''
        loja = []
        l = {}
        result = consultar_db(sql)
        for i in result:
            l = {"id": i[0], "nota": i[6] }
            loja.append(l)
        cont = 0
        for l in loja:
            if l['id'] == id_loja:
                novaNota = int(l['nota'])
                novaNota += nota
                novaNota = novaNota/2
            elif l['id'] != id_loja:
                cont = cont + 1
            if cont == len(loja):
                return 'Esse id não pertence a lista de lojas!'
        sql = '''
        UPDATE loja SET nota=?
        WHERE cpf=?;
        '''
        tupla = (novaNota, id_loja)
        inserir_db(sql, tupla)
        return 'Obrigado pela sua avaliação!'