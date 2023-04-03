from App.db import *
from App import Pedido


# Classe Entregador:

class ENTREGADOR(Base):
    __tablename__ = 'ENTREGADOR'
    id_entregador = Column('CPF', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME',String(255), nullable=False)
    telefone = Column('TELEFONE', String(15), nullable=False)
    id_pedido = Column('ID_PEDIDO', Integer, nullable=False)


    def __init__(self, id_entregador, nome, telefone):
        self.id_entregador = id_entregador
        self.nome = nome
        self.telefone = telefone


# Model da classe Entregador:


class Model_Entregador():

    def __init__(self):
        self.entregadores = []
        
    def adicionar_entregador(self, entregador):
        self.entregadores.append(entregador)
        
    def buscar_entregador(self, entregador_id):
        for entregador in self.entregadores:
            if entregador.id_entregador == entregador_id:
                return entregador
        return None
    
    def associar_entregador_pedido(self, entregador_id, pedido_id):
        entregador = self.buscar_entregador(entregador_id)
        if entregador:
            pedido = Pedido.Model_Pedido.buscar_pedido(pedido_id)
            if pedido:
                pedido.entregador = entregador
                return True
        return False