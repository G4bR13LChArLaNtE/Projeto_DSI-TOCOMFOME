from .Model import Model_Vendedor

from flask import Blueprint, jsonify

vendedor_app = Blueprint('vendedor_app', __name__)

# Rotas Vendedor:


@vendedor_app.route('/vendedor/adicionar/<string:nome>/<string:usuario>/<string:telefone>/<string:email>/<string:data_nasc>', methods=['POST'])
def vendedorAdicionar(nome, usuario, telefone, email, data_nasc):
    return jsonify(Model_Vendedor.adicionar_vendedor(nome, usuario, telefone, email, data_nasc))


@vendedor_app.route("/vendedores", methods=["GET"])
def vendedores():
    return jsonify(Model_Vendedor.visualizar_vendedores())


@vendedor_app.route("/vendedor/<int:id_vendedor>", methods=["GET"])
def vendedor(id_vendedor):
    return jsonify(Model_Vendedor.visualizar_vendedor(id_vendedor))


@vendedor_app.route('/vendedor/atualizar/<int:id_vendedor>/<string:usuario>/<string:telefone>/<string:email>', methods=['PUT'])
def vendedorAtualizar(id_vendedor, usuario, telefone, email):
    return jsonify(Model_Vendedor.atualizar_vendedor(id_vendedor, usuario, telefone, email))


@vendedor_app.route("/vendedor/excluir/<int:id_vendedor>", methods=["POST"])
def vendedor_excluir(id_vendedor):
    return jsonify(Model_Vendedor.excluir_vendedor(id_vendedor))
