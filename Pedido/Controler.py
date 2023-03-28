from tocomfome import *
from Model import Model_Pedido



# Rotas Pedido:


# @app.route('/pedido/adicionar/<int:pedidos>/<int:qtdProduto>', methods=['POST'])
# def pedidoAdicionar(produtos, qtdProduto):
#     return jsonify(Model_Pedido.adicionar_pedido(produtos, qtdProduto))



@app.route("/pedido", methods=["GET"])
def pedidos():
    return jsonify(Model_Pedido.visualizar_pedidos())


@app.route("/pedido/<int:id_pedido>", methods=["GET"])
def produto(id_pedido):
    return jsonify(Model_Pedido.visualizar_pedido(id_pedido))


# @app.route('/estoque/atualizar/<int:id_item>/<int:produtos>/<int:qtdProduto>', methods=['PUT'])
# def produtoAtualizar(id_item, produtos, qtdProduto):
#     return jsonify(Model_Estoque.atualizar_item(id_item, produtos, qtdProduto))


@app.route("/pedido/excluir/<int:id_pedido>", methods=["POST"])
def produto_excluir(id_pedido):
    return jsonify(Model_Pedido.excluir_item(id_pedido))

@app.route("/pedido", methods=["GET"])
def pedido():
    return jsonify(Model_Pedido.buscar_pedido())