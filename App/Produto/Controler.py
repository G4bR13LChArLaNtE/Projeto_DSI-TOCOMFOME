from .Model import Model_Produto


from flask import Blueprint, jsonify


produto_app = Blueprint('produto_app', __name__)


# Rotas Produto:


@produto_app.route('/produto/adicionar/<string:nome>/<string:descricao>/<string:imagem>/<int:qtdProduto>/<float:valor>/<int:id_categoria>/<int:id_loja>', methods=['POST'])
def produtoAdicionar(nome, descricao, imagem, qtdProduto, valor, id_categoria, id_loja):
    return jsonify(Model_Produto.adicionar_produto(nome, descricao, imagem, qtdProduto, valor, id_categoria, id_loja))

@produto_app.route("/produtos", methods=["GET"])
def produtos():
    return jsonify(Model_Produto.visualizar_produtos())


@produto_app.route("/produto/<int:id_produto>", methods=["GET"])
def produto(id_produto):
    return jsonify(Model_Produto.visualizar_produtos(id_produto))


@produto_app.route("/produto/excluir/<int:id_produto>", methods=["POST"])
def produtoExcluir(id_produto):
    return jsonify(Model_Produto.excluir_produto(id_produto))

@produto_app.route('/produto/<id_produto>/<string:nome>', methods=['PUT'])
def produtoAtualizarNome(id_produto, nome):
    return jsonify(Model_Produto.atualizar_produtoNome(id_produto, nome))

@produto_app.route('/produto/<id_produto>/<string:descricao>', methods=['PUT'])
def produtoAtualizarDescricao(id_produto, descricao):
    return jsonify(Model_Produto.atualizar_produtoDescricao(id_produto, descricao))

@produto_app.route('/produto/<id_produto>/<string:imagem>', methods=['PUT'])
def produtoAtualizarImagem(id_produto, imagem):
    return jsonify(Model_Produto.atualizar_produtoImagem(id_produto, imagem))

@produto_app.route('/produto/<id_produto>/<int:qtdProduto>', methods=['PUT'])
def produtoAtualizarQtd(id_produto, qtdProduto):
    return jsonify(Model_Produto.atualizar_produtoQtd(id_produto, qtdProduto))

@produto_app.route('/produto/<id_produto>/<float:valor>', methods=['PUT'])
def produtoAtualizarValor(id_produto, valor):
    return jsonify(Model_Produto.atualizar_produtoValor(id_produto, valor))

@produto_app.route('/produto/<id_produto>/<int:id_categoria>', methods=['PUT'])
def produtoAtualizarCategoria(id_produto, id_categotia):
    return jsonify(Model_Produto.atualizar_produtoCategoria(id_produto, id_categotia))

@produto_app.route('/produto/<id_produto>/<int:id_loja>', methods=['PUT'])
def produtoAtualizarLoja(id_produto, id_loja):
    return jsonify(Model_Produto.atualizar_produtoLutoja(id_produto, id_loja))