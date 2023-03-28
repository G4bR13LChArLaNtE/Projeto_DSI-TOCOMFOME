from TOCOMFOME import *
from Model import *



# Rotas Loja:


@app.route('/loja/adicionar/<string:nome>/<string:descricao>/<string:logo>/<string:endereco>/<date:horario_func>/<int:nota>/<int:id_vendedor>', methods=['POST'])
def lojaAdicionar(nome, descricao, logo, endereco, horario_func, nota, id_vendedor):
    return jsonify(Model_Loja.adicionar_loja(nome, descricao, logo, endereco, horario_func, nota, id_vendedor))


@app.route("/lojas", methods=["GET"])
def lojas():
    return jsonify(Model_Loja.visualizar_lojas())


@app.route("/loja/<int:id_loja>", methods=["GET"])
def loja(id_loja):
    return jsonify(Model_Loja.visualizar_loja(id_loja))


@app.route('/loja/atualizar/<int:id_loja>/<string:nome>/<string:descricao>/<string:logo>/<string:endereco>/<string:horario_func>', methods=['PUT'])
def lojaAtualizar(id_loja, nome, descricao, logo, endereco, horario_func):
    return jsonify(Model_Loja.atualizar_loja(id_loja, nome, descricao, logo, endereco, horario_func))


@app.route("/loja/excluir/<int:id_loja>", methods=["POST"])
def lojaExcluir(id_loja):
    return jsonify(Model_Loja.excluir_loja(id_loja))
