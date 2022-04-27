from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'db/agrifacil.db'
db = SQLAlchemy(app)

conn = sqlite3.connect('db/agrifacil.db')
print ("Opened database successfully")

try:
    conn.execute('CREATE TABLE pedido (idPedido INTEGER PRIMARY KEY AUTOINCREMENT, idProdutor INTEGER, idProduto INTEGER, quantidade INTEGER, CPF INTEGER, valor FLOAT, horario DATETIME, uuid TEXT, status_pedido TEXT, FOREIGN KEY(idProdutor) REFERENCES produtor(idProdutor), FOREIGN KEY(CPF) REFERENCES consumidor(CPF), FOREIGN KEY(idProduto) REFERENCES produto(idProduto))')
    print ("Table created successfully")
    conn.close()
except Exception as e:
    print ("Table already exists")

class Pedido(db.Model):
    ID = db.Column ('idPedido', db.Integer, primary_key=True, unique=True)
    idProdutor = db.Column('idProdutor', db.Integer, unique=False, nullable=False)
    quantidade = db.Column('quantidade', db.Integer, unique=False, nullable=False)
    CPF = db.Column('CPF', db.Integer, unique=False, nullable=False)
    valor = db.Column('valor', db.Float, unique=False, nullable=False)
    horario = db.Column('horario', db.DateTime, unique=False, nullable=False)
    uuid = db.Column('uuid', db.String(800), unique=False, nullable=False)
    status_pedido = db.Column('status_pedido', db.String(800), unique=False, nullable=False)

    def __repr__(self):
        return f"user('{self.ID}', '{self.idProdutor}', '{self.quantidade}', '{self.CPF}', '{self.valor}', '{self.horario}', '{self.uuid}', '{self.status_pedido}')"
