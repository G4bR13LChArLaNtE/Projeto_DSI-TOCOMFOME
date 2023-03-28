from TOCOMFOME import *
from Model import *



# Rotas Estoque:


@app.route('/estoque/adicionar/<int:produtos>/<int:qtdProduto>', methods=['POST'])
def produtoAdicionar(produtos, qtdProduto):
    return jsonify(Model_Estoque.adicionar_item(produtos, qtdProduto))



@app.route("/estoque", methods=["GET"])
def produtos():
    return jsonify(Model_Estoque.visualizar_itens())


@app.route("/estoque/<int:id_item>", methods=["GET"])
def produto(id_item):
    return jsonify(Model_Estoque.visualizar_item(id_item))


@app.route('/estoque/atualizar/<int:id_item>/<int:produtos>/<int:qtdProduto>', methods=['PUT'])
def produtoAtualizar(id_item, produtos, qtdProduto):
    return jsonify(Model_Estoque.atualizar_item(id_item, produtos, qtdProduto))


@app.route("/estoque/excluir/<int:id_item>", methods=["POST"])
def produto_excluir(id_item):
    return jsonify(Model_Estoque.excluir_item(id_item))