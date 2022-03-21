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