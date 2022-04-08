from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'db/product.db'
db = SQLAlchemy(app)

conn = sqlite3.connect('db/product.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE produto (idProduto INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, categoria TEXT, quantidade INTEGER, preco REAL, idProdutor INTEGER, FOREIGN KEY(idProdutor) REFERENCES produtor(idProdutor))')
print ("Table created successfully")
conn.close()

class Produto(db.Model):
    idProduto = db.Column('idProduto', db.Integer, primary_key=True, unique=True)
    nomeProduto = db.Column('nome', db.String(80), unique=False, nullable=False)
    categoria = db.Column('categoria', db.String(80), unique=False, nullable=False)
    quantidade = db.Column('quantidade', db.Integer, unique=False, nullable=False)
    preco = db.Column('preco', db.Float, unique=False, nullable=False)
    idProdutor = db.Column('idProdutor', db.Integer, db.ForeignKey('produtor.idProdutor'),unique=False, nullable=False)

    def __repr__(self):
        return f"user('{self.idProduto}','{self.nomeProduto}', '{self.categoria}', '{self.quantidade}', '{self.preco}', '{self.idProdutor}')"
