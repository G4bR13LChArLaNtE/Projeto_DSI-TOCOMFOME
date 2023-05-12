from .Model import Model_Cliente


from flask import Blueprint, jsonify


cliente_app = Blueprint('cliente_app', __name__)


# Rotas Cliente:


@cliente_app.route('/cliente/adicionar/<string:cpf>/<string:nome>/<string:usuario>/<string:endereco>/<string:telefone>/<string:email>/<string:data_nasc>', methods=['POST'])
def clienteAdicionar(cpf, nome, usuario, endereco, telefone, email, data_nasc):
    return jsonify(Model_Cliente.adicionar_cliente(cpf, nome, usuario, endereco, telefone, email, data_nasc))


@cliente_app.route("/clientes", methods=["GET"])
def clientes():
    return jsonify(Model_Cliente.visualizar_clientes())


@cliente_app.route("/cliente/<int:id_cliente>", methods=["GET"])
def cliente(id_cliente):
    return jsonify(Model_Cliente.visualizar_cliente(id_cliente))


@cliente_app.route('/cliente/atualizar/<string:cpf>/<string:nome>/<string:usuario>/<string:endereco>/<string:telefone>/<string:email>/<string:data_nasc>', methods=['PUT'])
def clienteAtualizar(cpf, nome, usuario, endereco, telefone, email, data_nasc):
    return jsonify(Model_Cliente.atualizar_cliente(cpf, nome, usuario, endereco, telefone, email, data_nasc))

@cliente_app.route('/cliente/atualizar/nome/<string:cpf>/<string:nome>', methods=['PUT'])
def atualizarNome(cpf, nome):
    return jsonify(Model_Cliente.atualizar_nome(cpf, nome))

@cliente_app.route('/cliente/atualizar/usuario/<string:cpf>/<string:usuario>', methods=['PUT'])
def atualizarNome(cpf, usuario):
    return jsonify(Model_Cliente.atualizar_nome(cpf, usuario))

@cliente_app.route('/cliente/atualizar/endereco/<string:cpf>/<string:endereco>', methods=['PUT'])
def atualizarNome(cpf, endereco):
    return jsonify(Model_Cliente.atualizar_endereco(cpf, endereco))

@cliente_app.route('/cliente/atualizar/telefone/<string:cpf>/<string:telefone>', methods=['PUT'])
def atualizarNome(cpf, telefone):
    return jsonify(Model_Cliente.atualizar_endereco(cpf, telefone))

@cliente_app.route('/cliente/atualizar/email/<string:cpf>/<string:email>', methods=['PUT'])
def atualizarNome(cpf, email):
    return jsonify(Model_Cliente.atualizar_endereco(cpf, email))

@cliente_app.route('/cliente/atualizar/email/<string:cpf>/<string:email>', methods=['PUT'])
def atualizarNome(cpf, email):
    return jsonify(Model_Cliente.atualizar_endereco(cpf, email))

@cliente_app.route('/cliente/atualizar/data/<string:cpf>/<string:data_nasc>', methods=['PUT'])
def atualizarNome(cpf, data_nasc):
    return jsonify(Model_Cliente.atualizar_endereco(cpf, data_nasc))

@cliente_app.route("/cliente/excluir/<int:id_cliente>", methods=["POST"])
def cliente_excluir(id_cliente):
    return jsonify(Model_Cliente.excluir_cliente(id_cliente))

@cliente_app.route("/cliente/nota/<int:id_loja>/<int:nota>", methods=["POST"])
def loja_nota(id_loja, nota):
    return jsonify(Model_Cliente.adicionar_nota(id_loja, nota))
