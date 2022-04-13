from flask import render_template, request, Blueprint, session
from crud import products
from crud import producer

app = Blueprint("producer", "app")

@app.route('/producer/<id>', methods=['GET', 'POST'])
def restaurant(id):
    producer_info = producer.producer_info(id)
    product_info = products.get_products_from_producer(id)
    print(producer_info)
    print(product_info)
    return render_template("producer_info.html", info = producer_info, produto = product_info)
