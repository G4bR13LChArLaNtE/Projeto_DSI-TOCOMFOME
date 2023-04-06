from .Model import Model_Categoria

from flask import Blueprint, jsonify


categoria_app = Blueprint('categoria_app', __name__)


# Rotas Categoria:


@categoria_app.route('/categoria/adicionar/<string:nome>', methods=['POST'])
def categoriaAdicionar(nome):
    return jsonify(Model_Categoria.adicionar_categoria(nome))


@categoria_app.route("/categorias", methods=["GET"])
def categorias():
    return jsonify(Model_Categoria.visualizar_categorias())


@categoria_app.route("/categoria/<int:id_categoria>", methods=["GET"])
def categoria(id_categoria):
    return jsonify(Model_Categoria.visualizar_categoria(id_categoria))


@categoria_app.route('/categoria/atualizar/<int:id_categoria>/<string:nome>/', methods=['PUT'])
def categoriaAtualizar(id_categoria, nome):
    return jsonify(Model_Categoria.atualizar_categoria(id_categoria, nome))


@categoria_app.route("/categoria/excluir/<int:id_categoria>", methods=["POST"])
def categoriaExcluir(id_categoria):
    return jsonify(Model_Categoria.excluir_categoria(id_categoria))
