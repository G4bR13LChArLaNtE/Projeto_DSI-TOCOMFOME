from .Model import Model_Entregador


from flask import Blueprint, jsonify

entregador_app = Blueprint('entregador_app', __name__)


# Rotas Entregador:


@entregador_app.route('/entregador/adicionar/<string:nome>/<string:telefone>/<int:id_entregador>', methods=['POST'])
def entregadorAdicionar(id_entregador, nome, telefone):
    return jsonify(Model_Entregador.adicionar_entregador(nome, id_entregador, telefone))



@entregador_app.route("/entregadores", methods=["GET"])
def entregadores():
    return jsonify(Model_Entregador.buscar_entregador())


@entregador_app.route("/entregador/<int:id_entregador>", methods=["GET"])
def entregador(id_entregador):
    return jsonify(Model_Entregador.associar_entregador_pedido(id_entregador))