import sqlite3
from multiprocessing import connection

def conecta():
    conn = sqlite3.connect("banco_de_dados.db")
    if conn is not None:
        return conn
    else:
        print('Erro ao abrir uma conexão, tente abrir o CMD como administrador')

def addcontato(conn, nome, celular):
    sql = """INSERT OR IGNORE INTO freelancers(nome, celular) VALUES (?, ?)"""
    cursor = conn.cursor()
    cursor.execute(sql, (nome, celular))
    conn.commit()
    conn.close()

def buscacontatoativo(conn, nome):
    cursor = conn.cursor()
    if nome is None or nome == "" or nome == "TODOS":
        sql = """SELECT nome, celular from freelancers"""
        cursor.execute(sql)
    else:
        nome = nome.strip()
        sql = f"""SELECT nome, celular FROM freelancers WHERE nome like '%{nome}%' """
        cursor.execute(sql)
    resposta = cursor.fetchall()
    conn.close()
    return resposta

def bancodedados():
    conn = sqlite3.connect("banco_de_dados.db")
    sql = """CREATE TABLE IF NOT EXISTS freelancers(
        nome text DEFAULT '',
        celular text PRIMARY KEY
        );"""
    conn.execute(sql)
    conn.commit()
    conn.close()

bancodedados()