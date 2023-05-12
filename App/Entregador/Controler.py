from .Model import Model_Entregador


from flask import Blueprint, jsonify

entregador_app = Blueprint('entregador_app', __name__)


# Rotas Entregador:


@entregador_app.route('/entregador/adicionar/<string:cpf>/<string:nome>', methods=['POST'])
def Adicionar_entregador(id_entregador, nome):
    return jsonify(Model_Entregador.adicionar_entregador(nome, id_entregador))

@entregador_app.route('/entregador/excluir/<int:id_entregador>', methods=["DELETE"])
def excluir_entregador(id_entregador):
    return jsonify(Model_Entregador.excluir_entregador(id_entregador))

@entregador_app.route('/entregador/atualizar/nome/<int:id_entregador>/<string:nome>', methods=['PUT'])
def atualizar_entregador(id_entregador, nome):
    return jsonify(Model_Entregador.atualizar_entregador_nome(id_entregador, nome))

@entregador_app.route('/entregador/atualizar/cpf/<int:id_entregador>/<int:cpf>', methods=['PUT'])
def atualizar_entregador(id_entregador, cpf):
    return jsonify(Model_Entregador.atualizar_entregador_nome(id_entregador, cpf))

@entregador_app.route('/entregadores', methods=['GET'])
def entregadores():
    return jsonify(Model_Entregador.visualizar_entregadores())

@entregador_app.route('/entregador/<int:id_entregador>', methods=['GET'])
def entregadores(id_entregador):
    return jsonify(Model_Entregador.visualizar_entregadores(id_entregador))
