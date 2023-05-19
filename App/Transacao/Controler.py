from .Model import Model_Transacao


from flask import Blueprint, jsonify


transacao_app = Blueprint('transacao_app', __name__)



# Rotas Transacoes:

@transacao_app.route("/transacoes", methods=["GET"])
def estoques():
    return jsonify(Model_Transacao.visualizar_transacoes())

@transacao_app.route("/transacao/<int:id_pedido>/<int:id_produto>/<string:nome_produto>/<int:valor_produto>", methods=["POST"])
def adicionarProduto(id_pedido, id_produto, nome_produto, valor_produto):
    return jsonify(Model_Transacao.adicionar_produto(id_pedido, id_produto, nome_produto, valor_produto))

@transacao_app.route("/transacao/<int:id_pedido>/<float:desconto>", methods=["POST"])
def calcularTotal(id_pedido, desconto):
    return jsonify(Model_Transacao.calcular_valores(id_pedido, desconto))
