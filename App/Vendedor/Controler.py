from .Model import Model_Vendedor

from flask import Blueprint, jsonify

vendedor_app = Blueprint('vendedor_app', __name__)

# Rotas Vendedor:


@vendedor_app.route('/vendedor/adicionar/<int:cpf>/<string:nome>/<string:usuario>/<string:telefone>/<string:email>/<string:data_nasc>/id_loja', methods=['POST'])
def vendedorAdicionar(cpf, nome, usuario, telefone, email, data_nasc, id_loja):
    return jsonify(Model_Vendedor.adicionar_vendedor(cpf, nome, usuario, telefone, email, data_nasc, id_loja))


@vendedor_app.route("/vendedores", methods=["GET"])
def vendedores():
    return jsonify(Model_Vendedor.visualizar_vendedores())


@vendedor_app.route("/vendedor/<int:cpf_vendedor>", methods=["GET"])
def vendedor(cpf_vendedor):
    return jsonify(Model_Vendedor.visualizar_vendedor(cpf_vendedor))


@vendedor_app.route("/vendedor/excluir/<int:cpf_vendedor>", methods=["POST"])
def vendedor_excluir(cpf_vendedor):
    return jsonify(Model_Vendedor.excluir_vendedor(cpf_vendedor))


@vendedor_app.route('/vendedor/atualizar/<int:id_vendedor>/<string:nome>', methods=['PUT'])
def vendedorAtualizarNome(id_vendedor, nome):
    return jsonify(Model_Vendedor.atualizar_vendedorNome(id_vendedor, nome))


@vendedor_app.route('/vendedor/atualizar/<int:id_vendedor>/<string:usuario>', methods=['PUT'])
def vendedorAtualizarUsuario(id_vendedor, usuario):
    return jsonify(Model_Vendedor.atualizar_vendedorUsuario(id_vendedor, usuario))


@vendedor_app.route('/vendedor/atualizar/<int:id_vendedor>/<string:telefone>', methods=['PUT'])
def vendedorAtualizarUsuario(id_vendedor, telefone):
    return jsonify(Model_Vendedor.atualizar_vendedorTelefone(id_vendedor, telefone))


@vendedor_app.route('/vendedor/atualizar/<int:id_vendedor>/<string:email>', methods=['PUT'])
def vendedorAtualizarEmail(id_vendedor, email):
    return jsonify(Model_Vendedor.atualizar_vendedorEmail(id_vendedor, email))


@vendedor_app.route('/vendedor/atualizar/<int:id_vendedor>/<string:data_nasc>', methods=['PUT'])
def vendedorAtualizarData(id_vendedor, data_nasc):
    return jsonify(Model_Vendedor.atualizar_vendedorData(id_vendedor, data_nasc))


@vendedor_app.route('/vendedor/atualizar/<int:id_vendedor>/<int:id_loja>', methods=['PUT'])
def vendedorAtualizarLoja(id_vendedor, id_loja):
    return jsonify(Model_Vendedor.atualizar_vendedorLoja(id_vendedor, id_loja))