import sqlite3 as sql

def create(CNPJ, nome_oficial, nome_fantasia, password, email, telefone, rua, numero, bairro, cidade, estado,
                CEP, complemento, agroecologico, organico, individualColetiva):
    with sql.connect("db/producer.db") as con: 
        cur = con.cursor()
        cur.execute("INSERT into produtor (CNPJ, nomeOficial, nomeFantasia, password, telefone, email, complemento, agroecologico, rua, numero, bairro, cidade, estado, CEP, organico, individualColetiva) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (CNPJ, nome_oficial, nome_fantasia, password, telefone, email, complemento, 
            rua, numero, bairro, cidade, estado, CEP, agroecologico, organico, individualColetiva))
        con.commit()
        print("Record successfully added")

def read(CNPJ, password):
    with sql.connect("db/producer.db") as con:
        cur = con.cursor()
        login_approve = cur.execute("SELECT * from produtor where CNPJ = (?) and password = (?)",(CNPJ, password))
        return login_approve
# update
# delete