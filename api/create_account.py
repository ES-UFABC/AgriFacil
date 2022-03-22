from flask import render_template, request, redirect, session, Blueprint
import uuid

app = Blueprint("account_settings", "app")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            user = request.form['user']
            password = request.form['password']
            telefone = request.form['telefone']
            email = request.form['email']
            CPF = request.form['CPF']
            RG = request.form['RG']
            rua = request.form['rua']
            numero = request.form['numero']
            bairro = request.form['bairro']
            cidade = request.form['cidade']
            estado = request.form['estado']
            CEP = request.form['CEP']
        except Exception as e:
            return render_template("register_miss.html")
    return render_template("index.html")

@app.route('/register_producer', methods=['GET', 'POST'])
def register_restaurant():
    if request.method == 'POST':
        try:
            nome_registro = request.form['user']
            nome_fantasia = request.form['nome']
            password = request.form['password']
            telefone = request.form['telefone']        
            email = request.form['email']
            CNPJ = request.form['CNPJ']
            categoria = request.form['categoria']
            funcionamento = request.form['funcionamento']
            rua = request.form['rua']
            numero = request.form['numero']
            bairro = request.form['bairro']
            cidade = request.form['cidade']
            estado = request.form['estado']
            CEP = request.form['CEP']
        except Exception as e:
            return render_template("register_producer_miss.html")
    return render_template("producer_login.html") 