from Projeto_DSI import *
from Model import *



# Rotas Cliente:


@app.route('/cliente/adicionar/<string:nome>/<string:usuario>/<string:endereco>/<string:telefone>/<string:email>/<date:data_nasc>', methods=['POST'])
def vendedorAdicionar(nome, usuario, endereco, telefone, email, data_nasc):
    return jsonify(Model_Cliente.adicionar_cliente(nome, usuario, endereco, telefone, email, data_nasc))


@app.route("/clientes", methods=["GET"])
def vendedores():
    return jsonify(Model_Cliente.visualizar_clientes())


@app.route("/cliente/<int:id_cliente>", methods=["GET"])
def vendedor(id_cliente):
    return jsonify(Model_Cliente.visualizar_cliente(id_cliente))


@app.route('/cliente/atualizar/<int:id_cliente>/<string:usuario>/<string:telefone>/<string:email>', methods=['PUT'])
def vendedorAtualizar(id_cliente, usuario, endereco, telefone, email):
    return jsonify(Model_Cliente.atualizar_cliente(id_cliente, usuario, endereco, telefone, email))


@app.route("/cliente/excluir/<int:id_cliente>", methods=["POST"])
def vendedor_excluir(id_cliente):
    return jsonify(Model_Cliente.excluir_cliente(id_cliente))
