import sqlite3 as sql

def create(name, category, description, value, id_producer):
    with sql.connect("db/agrifacil.db") as con: 
        cur = con.cursor()
        cur.execute("INSERT into produto (nome, categoria, descricao, preco, idProdutor) VALUES (?, ?, ?, ?, ?)",(name, category, description, value, id_producer))
        con.commit()
        print("Record successfully added")

def get_products_from_producer(id):
    with sql.connect("db/agrifacil.db") as con: 
        cur = con.cursor()
        cur.execute("SELECT * from produto where idProdutor = (?)",(id))
        return cur.fetchall()