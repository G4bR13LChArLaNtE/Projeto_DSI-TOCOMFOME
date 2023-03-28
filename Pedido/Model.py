from TOCOMFOME import *



# Classe Estoque:

class PEDIDO(Base):
    __tablename__ = 'PEDIDO'
    id = Column('ID_PEDIDO', Integer, primary_key=True, autoincrement=True)
    id_produto = Column('ID_PRODUTO', Integer, nullable=False)
    nome_produto = Column('NOME_PRODUTO', String(40), nullable=True)
    valor_produto = Column('VALOR_PRODUTO', Double, nullable=False)
    total = Column('TOTAL', Double, nullable=False)
    status_pedido = Column('NOME_PRODUTO', String(20), nullable=True)
    entregue = Column('NOME_PRODUTO', String(10), nullable=True)
    data_pedido = Column('DATA_PEDIDO', Date, nullable=False)
    cpf_cliente = Column('CPF', Integer, nullable=False)
    observacao = Column('OBSERVACAO', String(40), nullable=True)
    pagamento  = Column('PAGAMENTO', String(20), nullable=True)
    desconto = Column('DESCONTO', Double, nullable=False)
    
    
    

    def __init__(self, id, id_produto, nome_produto, valor_produto, total, status_pedido, entregue, data_pedido, cpf_cliente, observacao, pagamento, desconto):
        self.id = id
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.valor_produto = valor_produto
        self.total = total
        self.status_pedido = status_pedido
        self.entregue = entregue
        self.data_pedido = data_pedido
        self.cpf_cliente = cpf_cliente
        self.observacao = observacao
        self.pagamento = pagamento
        self.desconto = desconto


# Model da classe Estoque:


class Model_Pedido():

    def visualizar_pedidos():
        sql = '''SELECT * FROM PEDIDO'''
        pedidos = []
        i = {}
        result = consultar_db(sql),
        for l in result:
            i = {"id": l[0], "id_produto": l[1], "nome_produto": l[2], "valor_produto": l[3], "total": l[4], "status_pedido": l[5], "entregue": l[6], "data_pedido": l[7], "cpf_cliente": l[8], "observacao": l[9], "pagamento": l[10], "desconto": l[11] }
            pedidos.append(i)
        return pedidos

    def visualizar_pedido(pedido_id):
        sql = '''SELECT * FROM ESTOQUE'''
        pedidos = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "id_produto": l[1], "nome_produto": l[2], "valor_produto": l[3], "total": l[4], "status_pedido": l[5], "entregue": l[6], "data_pedido": l[7], "cpf_cliente": l[8], "observacao": l[9], "pagamento": l[10], "desconto": l[11] }
            pedidos.append(i)
        cont = 0
        for i in pedidos:
            if i['id'] == pedido_id:
                return i
            elif i['id'] != pedido_id:
                cont = cont + 1
            if cont == len(pedidos):
                return 'Esse id não pertence a lista de pedidos!'

    # def adicionar_pedido(produto, qtdProduto):
    #     sql  = '''
    #     INSERT into pedido(produto, qtdProduto)
    #     values( '{}', '{}');
    #     '''.format(produto, qtdProduto)
    #     inserir_db(sql)
    #     return 'Item adicionado a lista com sucesso!'

    def excluir_item(pedido_id):
        sql = '''SELECT * FROM PEDIDO;'''
        pedidos = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "id_produto": l[1], "nome_produto": l[2], "valor_produto": l[3], "total": l[4], "status_pedido": l[5], "entregue": l[6], "data_pedido": l[7], "cpf_cliente": l[8], "observacao": l[9], "pagamento": l[10], "desconto": l[11] }
            pedidos.append(i)
        pedido_id = int(pedido_id)
        cont = 0
        for i in pedidos:
            if i['id'] == pedido_id:
                sql = '''
                Delete from pedido where id = {};
                '''.format(pedido_id)
                inserir_db(sql)
                return 'Item excluido com sucesso!'
            elif i['id'] != pedido_id:
                cont = cont + 1
            if cont == len(pedidos):
                return 'Esse id não pertence a lista de pedidos!'

    # def atualizar_item(pedido_id, produto, qtdProduto):
    #     sql = '''
    #     UPDATE estoque SET produto = '{}', qtdProduto='{}' 
    #     WHERE id={};
    #     '''.format(produto, qtdProduto, pedido_id)
    #     inserir_db(sql)
    #     return 'Atualizado com sucesso!'
    
    def buscar_pedido(self, pedido_id):
        for pedido in self.pedidos:
            if pedido.id == pedido_id:
                return pedido
        return None
    
    # A classe PedidoController permite adicionar novos pedidos e 
    # buscar pedidos pelo ID