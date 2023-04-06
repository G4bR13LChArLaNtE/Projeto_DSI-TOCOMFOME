from .Model import Model_Produto


from flask import Blueprint, jsonify


produto_app = Blueprint('produto_app', __name__)


# Rotas Produto:


@produto_app.route('/produto/adicionar/<string:nome>/<string:descricao>/<string:imagem>/<int:qtdProduto>/<float:valor>/<int:id_categoria>', methods=['POST'])
def produtoAdicionar(nome, descricao, imagem, qtdProduto, valor, id_categoria):
    return jsonify(Model_Produto.adicionar_produto(nome, descricao, imagem, qtdProduto, valor, id_categoria))



@produto_app.route("/produtos", methods=["GET"])
def produtos():
    return jsonify(Model_Produto.visualizar_produtos())


@produto_app.route("/produto/<int:id_produto>", methods=["GET"])
def produto(id_produto):
    return jsonify(Model_Produto.visualizar_produtos(id_produto))


@produto_app.route('/produto/<id_produto>/<string:nome>/<string:descricao>/<string:imagem>/<int:qtdProduto>/<float:valor>/<int:id_categoria>', methods=['PUT'])
def produtoAtualizar(id_produto, nome, descricao, imagem, qtdProduto, valor, id_categotia):
    return jsonify(Model_Produto.atualizar_produto(id_produto, nome, descricao, imagem, qtdProduto, valor, id_categotia))


@produto_app.route("/produto/excluir/<int:id_produto>", methods=["POST"])
def produtoExcluir(id_produto):
    return jsonify(Model_Produto.excluir_produto(id_produto))
