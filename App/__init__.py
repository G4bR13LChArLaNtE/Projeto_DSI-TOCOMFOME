from flask import Flask


from .Categoria.Controler import categoria_app
from .Cliente.Controler import cliente_app
from .Entregador.Controler import entregador_app
from .Estoque.Controler import estoque_app
from .Loja.Controler import loja_app
from .Pedido.Controler import pedido_app
from .Produto.Controler import produto_app
from .Vendedor.Controler import vendedor_app


app = Flask(__name__)


app.register_blueprint(categoria_app)
app.register_blueprint(cliente_app)
app.register_blueprint(entregador_app)
app.register_blueprint(estoque_app)
app.register_blueprint(loja_app)
app.register_blueprint(pedido_app)
app.register_blueprint(produto_app)
app.register_blueprint(vendedor_app)
