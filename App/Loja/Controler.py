from .Model import Model_Loja

from flask import Blueprint, jsonify

loja_app = Blueprint('loja_app', __name__)


# Rotas Loja:


@loja_app.route('/loja/adicionar/<string:nome>/<string:descricao>/<string:logo>/<string:endereco>/<string:horario_func>/<int:nota>/<int:id_vendedor>', methods=['POST'])
def lojaAdicionar(nome, descricao, logo, endereco, horario_func, nota, id_vendedor):
    return jsonify(Model_Loja.adicionar_loja(nome, descricao, logo, endereco, horario_func, nota, id_vendedor))


@loja_app.route("/loja/excluir/<int:id_loja>", methods=["POST"])
def lojaExcluir(id_loja):
    return jsonify(Model_Loja.excluir_loja(id_loja))


@loja_app.route("/lojas", methods=["GET"])
def lojas():
    return jsonify(Model_Loja.visualizar_lojas())


@loja_app.route("/loja/<int:id_loja>", methods=["GET"])
def loja(id_loja):
    return jsonify(Model_Loja.visualizar_loja(id_loja))


@loja_app.route('/loja/atualizar/<int:id_loja>/<string:nome>', methods=['PUT'])
def lojaAtualizarNome(id_loja, nome):
    return jsonify(Model_Loja.atualizar_nome(id_loja, nome))


@loja_app.route('/loja/atualizar/<int:id_loja>/<string: descricao>', methods=['PUT'])
def lojaAtualizarNome(id_loja, descricao):
    return jsonify(Model_Loja.atualizar_descricao(id_loja, descricao))


@loja_app.route('/loja/atualizar/<int:id_loja>/<string: logo>', methods=['PUT'])
def lojaAtualizarNome(id_loja, logo):
    return jsonify(Model_Loja.atualizar_logo(id_loja, logo))


@loja_app.route('/loja/atualizar/<int:id_loja>/<string: endereco>', methods=['PUT'])
def lojaAtualizarNome(id_loja, endereco):
    return jsonify(Model_Loja.atualizar_endereco(id_loja, endereco))


@loja_app.route('/loja/atualizar/<int:id_loja>/<string: horario>', methods=['PUT'])
def lojaAtualizarNome(id_loja, horario):
    return jsonify(Model_Loja.atualizar_horario(id_loja, horario))