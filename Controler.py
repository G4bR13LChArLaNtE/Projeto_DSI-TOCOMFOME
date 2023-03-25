from flask import Flask, jsonify, request

from Model import *


app = Flask(__name__)


# Rotas Vendedor:


@app.route('/vendedor/adicionar/<string:nome>/<string:usuario>/<string:telefone>/<string:email>/<date:data_nasc>', methods=['POST'])
def vendedorAdicionar(nome, usuario, telefone, email, data_nasc):
    return jsonify(Model_Vendedor.adicionar_vendedor(nome, usuario, telefone, email, data_nasc))


@app.route("/vendedores", methods=["GET"])
def vendedores():
    return jsonify(Model_Vendedor.visualizar_vendedores())


@app.route("/vendedor/<int:id_vendedor>", methods=["GET"])
def vendedor(id_vendedor):
    return jsonify(Model_Vendedor.visualizar_vendedor(id_vendedor))


@app.route('/vendedor/atualizar/<int:id_vendedor>/<string:usuario>/<string:telefone>/<string:email>', methods=['PUT'])
def vendedorAtualizar(id_vendedor, usuario, telefone, email):
    return jsonify(Model_Vendedor.atualizar_vendedor(id_vendedor, usuario, telefone, email))


@app.route("/vendedor/excluir/<int:id_vendedor>", methods=["POST"])
def vendedor_excluir(id_vendedor):
    return jsonify(Model_Vendedor.excluir_vendedor(id_vendedor))

# Rotas Produto:


@app.route('/produto/adicionar/<string:nome>/<string:descricao>/<string:imagem>/<int:qtdProduto>/<float:valor>', methods=['POST'])
def produtoAdicionar(nome, descricao, imagem, qtdProduto, valor):
    return jsonify(Model_Produto.adicionar_produto(nome, descricao, imagem, qtdProduto, valor))



@app.route("/produtos", methods=["GET"])
def produtos():
    return jsonify(Model_Produto.visualizar_produtos())


@app.route("/produto/<int:id_produto>", methods=["GET"])
def produto(id_produto):
    return jsonify(Model_Produto.visualizar_produtos(id_produto))


@app.route('/produto/<id_produto>/<string:nome>/<string:descricao>/<string:imagem>/<int:qtdProduto>/<float:valor>', methods=['PUT'])
def produtoAtualizar(id_produto, nome, descricao, imagem, qtdProduto, valor):
    return jsonify(Model_Produto.atualizar_produto(id_produto, nome, descricao, imagem, qtdProduto, valor))


@app.route("/produto/excluir/<int:id_produto>", methods=["POST"])
def produto_excluir(id_produto):
    return jsonify(Model_Produto.excluir_produto(id_produto))


# Rotas estoque:


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



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)