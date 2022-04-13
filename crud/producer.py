import sqlite3 as sql

def create(CNPJ, nome_oficial, nome_fantasia, password, email, telefone, rua, numero, bairro, cidade, estado,
                CEP, complemento, agroecologico, organico, individualColetiva):
    with sql.connect("db/producer.db") as con: 
        cur = con.cursor()
        cur.execute("INSERT into produtor (CNPJ, nomeOficial, nomeFantasia, password, telefone, email, complemento, agroecologico, rua, numero, bairro, cidade, estado, CEP, organico, individualColetiva) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (CNPJ, nome_oficial, nome_fantasia, password, telefone, email, complemento, 
            agroecologico, rua, numero, bairro, cidade, estado, CEP, organico, individualColetiva))
        con.commit()
        print("Record successfully added")

def read(CNPJ, password):
    with sql.connect("db/producer.db") as con:
        cur = con.cursor()
        login_approve = cur.execute("SELECT * from produtor where CNPJ = (?) and password = (?)",(CNPJ, password))
        return login_approve
    
def list_producers():
    with sql.connect("db/producer.db") as con:
        cur = con.cursor()
        cur.execute("SELECT idProdutor, nomeFantasia, organico, email from produtor")
        return cur.fetchall()

def producer_info(id):
    with sql.connect("db/producer.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * from produtor where idProdutor = (?)",(id,))
        return cur.fetchall()

# update
# delete