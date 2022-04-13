from flask import render_template, request, Blueprint, session
from crud import products
from crud import producer

app = Blueprint("products", "app")

@app.route('/main', methods=['GET', 'POST'])
def main():
    producer_list = producer.list_producers()
    return render_template("main.html", info = producer_list)

@app.route('/add-products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        try:
            name = request.form['name']
            description = request.form['description']
            value = request.form['valor']
            print(name, description, value, session['cnpj'])
            # products.create(name, description, value, session['cnpj'])
            print("Record successfully added")
        except Exception as e:
            print("bad")
    return render_template("products_set.html")