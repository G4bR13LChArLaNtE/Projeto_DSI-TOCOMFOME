from flask import Flask, jsonify, request
from sqlalchemy import Column, Integer, String, Date, Float, VARBINARY
from sqlalchemy.ext.declarative import declarative_base


import os

import pyodbc

from dotenv import load_dotenv


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

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

def inserir_db(sql, lista):
    con = conectar_db()
    cur = con.cursor()
    try:
        cur.execute(sql, lista)
        con.commit()
    except (Exception, pyodbc.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        return 1
    finally:
        cur.close()
        con.close()

def consultar_db(sql):
    con = conectar_db()
    cur = con.cursor()
    try:
        cur.execute(sql)
        recset = cur.fetchall()
        registros = []
        for rec in recset:
            registros.append(rec)
        return registros
    except (Exception, pyodbc.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        return 1
    finally:
        cur.close()
        con.close()