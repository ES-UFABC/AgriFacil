from flask import render_template, request, Blueprint, session
from crud import products
from crud import producer

app = Blueprint("producer", "app")

@app.route('/producer/<cnpj>', methods=['GET', 'POST'])
def restaurant(cnpj):
    producer_info = producer.producer_info(cnpj)
    # cur.execute("SELECT ID, produto,descricao,valor from cardapio where CNPJ={cnpj}".format(cnpj=cnpj))
    # produto_info = cur.fetchall()
    # print(produto_info)
    product_info = ' teste'
    return render_template("restaurant_info.html", info = producer_info, produto = product_info)