from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'db/agrifacil.db'
db = SQLAlchemy(app)

conn = sqlite3.connect('db/agrifacil.db')
print ("Opened database successfully")

try:
    conn.execute('CREATE TABLE produto (idProduto INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, categoria TEXT, descricao TEXT, preco REAL, idProdutor INTEGER, FOREIGN KEY(idProdutor) REFERENCES produtor(idProdutor))')
    print ("Table created successfully")
    conn.close()
except Exception as e:
    print ("Table already exists")

class Produto(db.Model):
    idProduto = db.Column('idProduto', db.Integer, primary_key=True, unique=True)
    nomeProduto = db.Column('nome', db.String(80), unique=False, nullable=False)
    categoria = db.Column('categoria', db.String(80), unique=False, nullable=False)
    quantidade = db.Column('descricao', db.Integer, unique=False, nullable=False)
    preco = db.Column('preco', db.Float, unique=False, nullable=False)
    idProdutor = db.Column('idProdutor', db.Integer, db.ForeignKey('produtor.idProdutor'),unique=False, nullable=False)

    def __repr__(self):
        return f"user('{self.idProduto}','{self.nomeProduto}', '{self.categoria}', '{self.descricao}', '{self.preco}', '{self.idProdutor}')"
