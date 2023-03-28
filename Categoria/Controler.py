from TOCOMFOME import *
from Model import *



# Rotas Categoria:


@app.route('/categoria/adicionar/<string:nome>', methods=['POST'])
def vendedorAdicionar(nome):
    return jsonify(Model_Categoria.adicionar_categoria(nome))


@app.route("/categorias", methods=["GET"])
def vendedores():
    return jsonify(Model_Categoria.visualizar_categorias())


@app.route("/categoria/<int:id_categoria>", methods=["GET"])
def vendedor(id_categoria):
    return jsonify(Model_Categoria.visualizar_categoria(id_categoria))


@app.route('/categoria/atualizar/<int:id_categoria>/<string:nome>/', methods=['PUT'])
def vendedorAtualizar(id_categoria, nome):
    return jsonify(Model_Categoria.atualizar_categoria(id_categoria, nome))


@app.route("/categoria/excluir/<int:id_categoria>", methods=["POST"])
def vendedor_excluir(id_categoria):
    return jsonify(Model_Categoria.excluir_categoria(id_categoria))