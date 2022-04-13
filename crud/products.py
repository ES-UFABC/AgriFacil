import sqlite3 as sql

def create(name, description, value, cnpj):
    with sql.connect("db/producer.db") as con: 
        cur = con.cursor()
        cur.execute("INSERT into produtos (produto, descricao, valor, CNPJ) VALUES (?, ?, ?, ?)",(name, description, value, cnpj))
        con.commit()
        print("Record successfully added")