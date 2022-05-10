import sqlite3 as sql

def create(idProdutor, idProduto, quantidade, CPF, order_number, status):
    with sql.connect("db/agrifacil.db") as con:
        cur = con.cursor()
        cur.execute("INSERT into pedido (idProdutor, idProduto, quantidade, CPF, uuid, status_pedido) VALUES (?,?,?,?,?,?)",(idProdutor, idProduto, quantidade, CPF, order_number, status))
        con.commit()
        print("Record successfully added")     

def get_order_info(order_id):
    with sql.connect("db/agrifacil.db") as con: 
        cur = con.cursor()
        cur.execute("SELECT r.nomeFantasia, c.nome, p.quantidade, c.preco from pedido p join produtor r on (p.idProdutor = r.idProdutor) join produto c on (p.idProduto = c.idProduto) where uuid=(?) and status_pedido='Pendente'",(order_id,))
        return cur.fetchall() 
    
def update(order_id, today, total):
    with sql.connect("db/agrifacil.db") as con:
        cur = con.cursor()
        cur.execute("UPDATE pedido set status_pedido = 'Confirmado', horario = (?), valor = (?) where uuid = (?)",(today, total, order_id))
        con.commit()
        print("Record successfully added")

def get_order_status(order_id):
    with sql.connect("db/agrifacil.db") as con: 
        cur = con.cursor()
        cur.execute("SELECT r.nomeFantasia, p.horario, c.preco, p.quantidade, p.status_pedido from pedido p join produtor r on (p.idProdutor = r.idProdutor) join produto c on (p.idProduto = c.idProduto) where uuid=(?) and status_pedido='Confirmado'",(order_id,))
        return cur.fetchall() 

def get_order_history(cpf):
    with sql.connect("db/agrifacil.db") as con: 
        cur = con.cursor()
        cur.execute("SELECT p.idPedido, p.valor, pr.nomeFantasia, p.horario FROM pedido p join produtor pr on (p.idProdutor = pr.idProdutor) join produto pt on (p.idProduto = pt.idProdutor) where p.cpf = (?) and p.status_pedido = 'Confirmado' group by idPedido",(cpf,))
        return cur.fetchall() 

def get_sell_history(id):
    with sql.connect("db/agrifacil.db") as con: 
        cur = con.cursor()
        cur.execute("SELECT p.idPedido, p.valor, c.nome, c.email, c.telefone, p.horario FROM pedido p join produtor pr on (p.idProdutor = pr.idProdutor) join consumidor c on (p.CPF = c.CPF) where p.idProdutor = (?) and p.status_pedido = 'Confirmado' group by idPedido",(id,))
        return cur.fetchall() 