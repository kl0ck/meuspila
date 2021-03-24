# https://docs.python.org/3/library/sqlite3.html
import sqlite3

class Database:

    con = sqlite3.connect(':memory:')

    def __init__(self):
        con = self.con
        c = con.cursor()

        c.execute("CREATE TABLE operacao (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT, cv TEXT, qtd TEXT, ticker TEXT, preco TEXT, nota TEXT)")

        con.commit()

    def add(self, operacao):
        con = self.con
        c = con.cursor()

        p = operacao.data, operacao.cv, operacao.qtd, operacao.ticker, operacao.preco, operacao.nota
        c.execute("INSERT INTO operacao (data, cv, qtd, ticker, preco, nota) VALUES (?, ?, ?, ?, ?, ?)", p)

        con.commit()

    def list(self):
        con = self.con
        c = con.cursor()

        c.execute("SELECT * FROM operacao")

        rows = c.fetchall()

        for r in rows:
            print(r)
