####### Imports #######
import json
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from item import Item
from cart import Cart

####### Setup/Config #######
app = Flask(__name__)
cors = CORS(app)
SECRET_KEY = 'SECRET_KEY'
app.config['SECRET_KEY'] = SECRET_KEY
api = Api(app)

####### Initialize Cart #######
cart = Cart()

####### Route Decorators #######


@app.route('/', methods=['POST', 'GET', 'UPDATE', 'DELETE'])
@cross_origin()
def index():
    if (request.method == 'POST'):
        itemData = request.get_json()
        # Initialize Item
        item = Item(
            itemData['id'], itemData['item_name'], itemData['item_price'], itemData['item_amount'])

        print(item.id)
        print(item.name)
        print(item.price)
        print(item.quantity)

        cart.addItem(item)

    if (request.method == "UPDATE"):
        itemData = request.get_json()
        # Initialize Item
        item = Item(
            itemData['id'], itemData['item_name'], itemData['item_price'], itemData['item_amount'])

        cart.updateItem(item)
        # return {
        #     'name': jsonData
        # }
        print(item.id)
        print(item.name)
        print(item.price)
        print(item.quantity)

    if (request.method == "GET"):
        pass

    if (request.method == "DELETE"):
        cart.itemList.removeItem()

    return render_template("index.html")


####### Run Applications #######
if __name__ == '__main__':
    app.run(debug=True)
