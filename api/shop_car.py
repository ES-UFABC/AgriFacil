import datetime
from flask import render_template, request, Blueprint, session

from crud import order as order_crud

app = Blueprint("shop", "app")

@app.route('/shop/<producer_id>', methods=['GET', 'POST'])
def shop(producer_id):
    if request.method == 'POST':    
        try:
            order_number = session['uuid']
            for requests in request.form:
                if request.form[requests] != "":  
                    id_produto = requests  
                    quantity = request.form[requests]
                    order_crud.create(producer_id, id_produto, quantity, session['cpf'], order_number, status = "Pendente")        
        except Exception as e:
            print(e)
        return ('', 204)

@app.route('/shop_car', methods=['GET', 'POST'])
def shop_car():
    order_number = session['uuid']
    try:
        shop_info = order_crud.get_order_info(order_number)
        total=0
        for product in shop_info:
            total = total + (product[2]*product[3])
        print(total)
        if total == 0:
            return render_template("empty_shop_car.html")
        return render_template("shop_car.html", shop_info=shop_info, total=round(total,2)) 
    except Exception as e:
        print(e)

@app.route('/order', methods=['GET', 'POST'])
def order():
    order_number = session['uuid']
    today = datetime.datetime.today().replace(second=0, microsecond=0)
    try:
        order_crud.update(order_number, today)
    except Exception as e:
        print(e)
    return ('', 204) 

@app.route('/order_status', methods=['GET', 'POST'])
def order_status():
    try:
        order_number = session['uuid']
        order_info = order_crud.get_order_status(order_number)
        total=0
        for product in order_info:
            total = total + (product[2]*product[3])
    except Exception as e:
        print(e)
    if total == 0:
        return render_template("empty_order.html")
    else:
        return render_template("order.html",  order=order_info, order_number=order_number, total=total)