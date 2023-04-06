from .Model import Model_Estoque


from flask import Blueprint, jsonify


estoque_app = Blueprint('estoque_app', __name__)



# Rotas Estoque:


@estoque_app.route('/estoque/adicionar/<int:produtos>/<int:qtdProduto>', methods=['POST'])
def estoqueAdicionar(produtos, qtdProduto):
    return jsonify(Model_Estoque.adicionar_item(produtos, qtdProduto))



@estoque_app.route("/estoque", methods=["GET"])
def estoques():
    return jsonify(Model_Estoque.visualizar_itens())


@estoque_app.route("/estoque/<int:id_item>", methods=["GET"])
def estoque(id_item):
    return jsonify(Model_Estoque.visualizar_item(id_item))


@estoque_app.route('/estoque/atualizar/<int:id_item>/<int:produtos>/<int:qtdProduto>', methods=['PUT'])
def estoqueAtualizar(id_item, produtos, qtdProduto):
    return jsonify(Model_Estoque.atualizar_item(id_item, produtos, qtdProduto))


@estoque_app.route("/estoque/excluir/<int:id_item>", methods=["POST"])
def estoqueExcluir(id_item):
    return jsonify(Model_Estoque.excluir_item(id_item))

