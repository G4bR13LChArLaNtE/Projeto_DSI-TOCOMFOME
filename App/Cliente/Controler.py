from .Model import Model_Cliente


from flask import Blueprint, jsonify


cliente_app = Blueprint('cliente_app', __name__)


# Rotas Cliente:


@cliente_app.route('/cliente/adicionar/<string:nome>/<string:usuario>/<string:endereco>/<string:telefone>/<string:email>/<string:data_nasc>', methods=['POST'])
def clienteAdicionar(nome, usuario, endereco, telefone, email, data_nasc):
    return jsonify(Model_Cliente.adicionar_cliente(nome, usuario, endereco, telefone, email, data_nasc))


@cliente_app.route("/clientes", methods=["GET"])
def clientes():
    return jsonify(Model_Cliente.visualizar_clientes())


@cliente_app.route("/cliente/<int:id_cliente>", methods=["GET"])
def cliente(id_cliente):
    return jsonify(Model_Cliente.visualizar_cliente(id_cliente))


@cliente_app.route('/cliente/atualizar/<int:id_cliente>/<string:usuario>/<string:endereco>/<string:telefone>/<string:email>', methods=['PUT'])
def clienteAtualizar(id_cliente, usuario, endereco, telefone, email):
    return jsonify(Model_Cliente.atualizar_cliente(id_cliente, usuario, endereco, telefone, email))


@cliente_app.route("/cliente/excluir/<int:id_cliente>", methods=["POST"])
def cliente_excluir(id_cliente):
    return jsonify(Model_Cliente.excluir_cliente(id_cliente))
