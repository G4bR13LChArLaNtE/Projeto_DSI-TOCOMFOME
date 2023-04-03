from App import app


from Categoria.Controler import *
from Cliente.Controler import *
from Entregador.Controler import *
from Estoque.Controler import *
from Loja.Controler import *
from Pedido.Controler import *
from Produto.Controler import *
from Vendedor.Controler import *




app.register_blueprint(categoria_app)
app.register_blueprint(cliente_app)
app.register_blueprint(entregador_app)
app.register_blueprint(estoque_app)
app.register_blueprint(loja_app)
app.register_blueprint(pedido_app)
app.register_blueprint(produto_app)
app.register_blueprint(vendedor_app)
