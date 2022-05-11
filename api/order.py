from flask import render_template, session, Blueprint
from crud import order 

app = Blueprint("order", "app")

@app.route('/order-history', methods=['GET', 'POST'])
def order_history():
    order_history = order.get_order_history(session['cpf'])
    print(order_history)
    return render_template("order_history.html", order_history = order_history)

@app.route('/sell-history', methods=['GET', 'POST'])
def sell_history():
    sell_history = order.get_sell_history(session['id'])
    for item in sell_history:
        print(item)
    return render_template("sell_history.html", sell_history = sell_history)