import sqlite3 as sql

def create(CPF, nome, password, email, telefone, rua, numero, bairro, cidade, estado, CEP, complemento):
    print("ok")
    with sql.connect("db/client.db") as con:
        cur = con.cursor()
        cur.execute("INSERT into consumidor (CPF, nome, password, telefone, email, rua, numero, bairro, cidade, estado, CEP, complemento) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
            (CPF, nome, password, telefone, email, rua, numero, bairro, cidade, estado, CEP, complemento))
        con.commit()
        print("Record successfully added")

def read(CPF, password):
    with sql.connect("db/client.db") as con:
        cur = con.cursor()
        login_approve = cur.execute("SELECT * from consumidor where CPF = (?) and password = (?)",(CPF, password))
        return login_approve

# update
# delete