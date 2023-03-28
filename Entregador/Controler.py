from tocomfome import *
from Model import Model_Entregador



# Rotas Entregador:


@app.route('/entregador/adicionar/<string:nome>/<string:telefone>/<int:id_entregador>', methods=['POST'])
def produtoAdicionar(id_entregador, nome, telefone):
    return jsonify(Model_Entregador.adicionar_entregador(nome, id_entregador, telefone))



@app.route("/entregador", methods=["GET"])
def entregador():
    return jsonify(Model_Entregador.buscar_entregador())


@app.route("/entregador/<int:id_entregador>", methods=["GET"])
def produto(id_entregador):
    return jsonify(Model_Entregador.associar_entregador_pedido(id_entregador))