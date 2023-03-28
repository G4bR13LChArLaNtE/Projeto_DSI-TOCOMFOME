from flask import Flask, jsonify, request
from sqlalchemy import Column, Integer, String, Date, Double
from sqlalchemy.ext.declarative import declarative_base


import os

import pyodbc

from dotenv import load_dotenv


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

senha = os.environ.get('PASS')


senha = os.environ.get('PASS')


server = 'CHARLANTEPC\SQLEXPRESS' # to specify an alternate port
database = 'APP_TOCOMFOME'




def conectar_db():
    con = pyodbc.connect('DRIVER={SQL Server};' +
                         'SERVER='+server+';' +
                         'DATABASE='+database+';'+
                         'Trusted_Connection=yes;')
    return con



Base = declarative_base(conectar_db())


# Métodos do banco de dados:

def inserir_db(sql):
    con = conectar_db()
    cur = con.cursor()
    try:
        cur.execute(sql)
        con.commit()
    except (Exception, pyodbc.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    finally:
        cur.close()

def consultar_db(sql):
    con = conectar_db()
    cur = con.cursor()
    try:
        cur.execute(sql)
        recset = cur.fetchall()
        registros = []
        for rec in recset:
            registros.append(rec)
        con.close()
        return registros
    except (Exception, pyodbc.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    finally:
        cur.close()



import Categoria.Controler
import Cliente.Controler
import Entregador.Controler
import Estoque.Controler
import Loja.Controler
import Pedido.Controler
import Produto.Controler
import Vendedor.Controler


app = Flask(__name__)

