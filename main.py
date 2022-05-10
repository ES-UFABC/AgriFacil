import os
import core.settings as st
from flask import Flask
from api.login import app as login_router
from api.create_account import app as account_router
from api.products import app as products_router
from api.producer import app as producer_router
from api.shop_car import app as shop_car_router

CONFIG_FILES = os.path.join('static')

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint(login_router)
app.register_blueprint(account_router)
app.register_blueprint(products_router)
app.register_blueprint(producer_router)
app.register_blueprint(shop_car_router)

if __name__ == '__main__':
    app.run(debug = True, port = st.PORT)
