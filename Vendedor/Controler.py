from Projeto_DSI import *
from Model import *



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
