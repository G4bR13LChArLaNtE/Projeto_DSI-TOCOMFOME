from Model import Model_Pedido

from flask import Blueprint, jsonify

pedido_app = Blueprint('pedido_app', __name__)

# Rotas Pedido:


@pedido_app.route('/pedido/adicionar/<int:pedidos>/<int:qtdProduto>', methods=['POST'])
def pedidoAdicionar(produtos, qtdProduto):
     return jsonify(Model_Pedido.adicionar_pedido(produtos, qtdProduto))


@pedido_app.route("/pedidos", methods=["GET"])
def pedidos():
    return jsonify(Model_Pedido.visualizar_pedidos())


@pedido_app.route("/pedido/<int:id_pedido>", methods=["GET"])
def pedido(id_pedido):
    return jsonify(Model_Pedido.visualizar_pedido(id_pedido))


@pedido_app.route('/pedido/atualizar/<int:id_item>/<int:produtos>/<int:qtdProduto>', methods=['PUT'])
def produtoAtualizar(id_item, produtos, qtdProduto):
     return jsonify(Model_Pedido.atualizar_item(id_item, produtos, qtdProduto))


@pedido_app.route("/pedido/excluir/<int:id_pedido>", methods=["POST"])
def pedidoExcluir(id_pedido):
    return jsonify(Model_Pedido.excluir_item(id_pedido))