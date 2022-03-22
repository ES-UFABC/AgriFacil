from flask import render_template, request, redirect, session, Blueprint
import uuid

app = Blueprint("account_settings", "app")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            #idConsumidor = criar função para puxar o último idConsumidor
            CPF = request.form['CPF']
            nome = request.form['nome']
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
        except Exception as e:
            return render_template("register_miss.html")
    return render_template("index.html")

@app.route('/register_producer', methods=['GET', 'POST'])
def register_restaurant():
    if request.method == 'POST':
        try:
            #idProdutor = criar função para puxar o último idProdutor
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
        except Exception as e:
            return render_template("register_producer_miss.html")
    return render_template("producer_login.html") 