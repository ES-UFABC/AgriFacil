from flask import render_template, request, redirect, session, Blueprint
import uuid

app = Blueprint("login", "app")

@app.route('/', methods=['GET', 'POST'])
def index():
    if "cpf" in session:
        return redirect("/main")
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
                login_approve = [['123']]
                for rows in login_approve:
                    session_cpf = rows[0]
                if session_cpf != None:
                    session['cpf'] = session_cpf
                    session['uuid'] = str(uuid.uuid4())
                else:
                    print("Don't have credentials")
                return redirect("/main")
            except Exception as e:
                return 'error'

@app.route('/main', methods=['GET', 'POST'])
def main():
    # Extrair informações dos produtos para renderizar no front
    return render_template("main.html") 

# Criar Rota de registro de usuário
# Criar Rota de registro de fornecedor
# Criar Rota de compra
# Criar Rota de Produtos

@app.route('/logout')
def logout():
    session.pop('cpf', None)

    return redirect("/", code=302)   