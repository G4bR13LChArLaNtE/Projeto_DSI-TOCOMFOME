from App.db import *



# Classe Pedido:

class PEDIDO(Base):
    __tablename__ = 'PEDIDO'
    id = Column('ID_PEDIDO', Integer, primary_key=True, autoincrement=True)
    total = Column('TOTAL', Float, nullable=True)
    status_pedido = Column('STATUS', String(20), nullable=False)
    data_pedido = Column('DATA_PEDIDO', Date, nullable=False)
    cpf_cliente = Column('CPF_CLIENTE', Integer, nullable=False)
    observacao = Column('OBSERVACAO', String(400), nullable=True)
    pagamento  = Column('PAGAMENTO', String(20), nullable=True)
    desconto = Column('DESCONTO', Float, nullable=True)
    id_entregador = Column('ID_ENTREGADOR', Integer, nullable=False)

    def __init__(self, total, status_pedido, data_pedido, cpf_cliente, observacao, pagamento, desconto, id_entregador):
        total = 0
        self.__total = total
        self.status_pedido = status_pedido
        self.data_pedido = data_pedido
        self.cpf_cliente = cpf_cliente
        self.observacao = observacao
        self.pagamento = pagamento
        desconto = 0
        self.desconto = desconto
        self.id_entregador = id_entregador

    def get_total(self):
        return self.__total

    def set_total(self, valor_produtos, desconto):
        self.__total = 0
        for v in valor_produtos:
            self.__total += v
        self.__total = self.__total * desconto


# Model da classe Pedido:


class Model_Pedido():

    def visualizar_pedidos():
        sql1 = '''SELECT * FROM PEDIDO'''
        pedidos = []
        i = {}
        result1 = consultar_db(sql1),
        for l in result1:
            i = {"id": l[0], "total": l[1], "status_pedido": l[2], "data_pedido": l[3], "cpf_cliente": l[4], "observacao": l[5], "pagamento": l[6], "desconto": l[7], "id_entregador": l[8] }
            pedidos.append(i)
        if len(pedidos) == 0:
            return "Não há pedido cadastrado!"
        else:
            sql2 = "SELECT * FROM TRANSACAO"
            result2 = consultar_db(sql2)
            for m in result2:
                m = {"id_transacao": l[0], "id_pedido": l[1], "id_produto": l[2], "nome_produto": l[3], "valor_produto": l[4]}
            pedidos["transacoes"] = m
            return pedidos

    def excluir_item(pedido_id):
        sql = '''SELECT * FROM PEDIDO;'''
        pedidos = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "total": l[1], "status_pedido": l[2], "data_pedido": l[3], "cpf_cliente": l[4], "observacao": l[5], "pagamento": l[6], "desconto": l[7], "id_entregador": l[8] }
            pedidos.append(i)
        pedido_id = int(pedido_id)
        cont = 0
        for i in pedidos:
            if i['id'] == pedido_id:
                sql = '''
                Delete from pedido where id = ?;
                Delete from transacao where id_pedido = ?;
                '''
                inserir_db(sql, pedido_id, pedido_id)
                return 'Pedido excluido com sucesso!'
            elif i['id'] != pedido_id:
                cont = cont + 1
            if cont == len(pedidos):
                return 'Esse id não pertence a lista de pedidos!'

    def adicionar_pedido(status_pedido, data_pedido, cpf_cliente, observacao, pagamento, desconto, id_entregador):
        sql  = '''
        INSERT into pedido(status_pedido, data_pedido, cpf_cliente, observacao, pagamento, desconto, id_entregador)
        values( ?, ?, ?, ?, ?, ?, ?);
        '''
        tupla = (status_pedido, data_pedido, cpf_cliente, observacao, pagamento, desconto, id_entregador)
        inserir_db(sql, tupla)
        return 'Pedido adicionado a lista com sucesso!'
