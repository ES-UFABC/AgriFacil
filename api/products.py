from flask import render_template, request, Blueprint, session
from crud import products as prdct
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
            category = request.form['category']
            description = request.form['description']
            value = request.form['valor']
            prdct.create(name, category, description, value, session['id'])
            print("Record successfully added")
        except Exception as e:
            print("bad")
    return render_template("products_set.html")

@app.route('/get-products', methods=['GET', 'POST'])
def get_products_list():
    
    return "Lista de produtos de um produtor" #ToDo

@app.route('/update-products', methods=['PUT'])
def update_products():
    
    return "Podutor pode atualizar informação de um produto" #ToDo