from flask import render_template, request, redirect, session, Blueprint
import uuid
from crud import client 
from crud import producer 

app = Blueprint("login", "app")

@app.route('/', methods=['GET', 'POST'])
def index():
    if "cpf" in session:
        return redirect("/main")
    elif "cnpj" in session:
        return render_template("main_producer.html")
    else:
        return render_template("index.html")

@app.route('/access', methods=['GET', 'POST'])
def access():
    if request.method == 'POST':
        if request.form['index'] == "Login":
            try:
                CPF = request.form['CPF']
                password = request.form['password']
                # Criar banco de dados e realizar consulta de login, por hora vamos simular o retorno da consulta
                login_approve = client.read(CPF, password)
                for rows in login_approve:
                    session_cpf = rows[0]
                if session_cpf != None:
                    session['cpf'] = session_cpf
                    session['uuid'] = str(uuid.uuid4())
                else:
                    print("Don't have credentials")
                return redirect("/main")
            except Exception as e:
                return render_template("index_denied.html") # Precisa criar
        elif request.form['index'] == "Registrar":
            return render_template("register.html")
        else:
            return render_template("producer_login.html")

@app.route('/access_producer', methods=['GET', 'POST'])
def access_producer():
    if request.method == 'POST':
        if request.form['index'] == "Login":
            try:
                CNPJ = request.form['CNPJ']
                password = request.form['password']
                login_approve = producer.read(CNPJ, password)
                for rows in login_approve:
                    session_cnpj = rows[0]
                if session_cnpj != None:
                    session['cnpj'] = session_cnpj
                else:
                    print("Don't have credentials")
                return render_template("main_producer.html")
            except Exception as e:
                return render_template("producer_login_denied.html") # Precisa criar
        else:
            return render_template("register_producer.html")

@app.route('/main', methods=['GET', 'POST'])
def main():
    # Extrair informações dos produtos para renderizar no front
    return render_template("main.html") 

@app.route('/logout')
def logout():
    session.pop('cpf', None)
    session.pop('cnpj', None)

    return redirect("/", code=302)  


