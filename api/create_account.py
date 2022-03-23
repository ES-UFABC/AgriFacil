from flask import render_template, request, Blueprint
from crud import client 
from crud import producer 

app = Blueprint("account_settings", "app")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            CPF = request.form['CPF']
            nome = request.form['user']
            password = request.form['password']
            email = request.form['email']
            telefone = request.form['telefone']
            rua = request.form['rua']
            numero = request.form['numero']
            bairro = request.form['bairro']
            cidade = request.form['cidade']
            estado = request.form['estado']
            CEP = request.form['CEP']
            complemento = request.form['complemento']
            client.create(CPF, nome, password, email, telefone, rua, numero, bairro, cidade, estado, CEP, complemento)
        except Exception as e:
            return render_template("register_miss.html")
    return render_template("index.html")

@app.route('/register_producer', methods=['GET', 'POST'])
def register_producer():
    if request.method == 'POST':
        try:
            CNPJ = request.form['CNPJ']
            nome_oficial = request.form['nome_oficial']
            nome_fantasia = request.form['nome_fantasia']
            password = request.form['password']
            email = request.form['email']
            telefone = request.form['telefone']        
            rua = request.form['rua']
            numero = request.form['numero']
            bairro = request.form['bairro']
            cidade = request.form['cidade']
            estado = request.form['estado']
            CEP = request.form['CEP']
            complemento = request.form['complemento']
            agroecologico = request.form['agroecologico']
            organico = request.form['organico']
            individualColetiva = request.form['individualColetiva']
            producer.create(CNPJ, nome_oficial, nome_fantasia, password, email, telefone, rua, numero, bairro, cidade, estado,
                CEP, complemento, agroecologico, organico, individualColetiva)
        except Exception as e:
            return render_template("register_producer_miss.html")
    return render_template("producer_login.html") 