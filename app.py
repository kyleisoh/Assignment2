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


@app.route('/', methods=['POST', 'GET', 'DELETE'])
@cross_origin()
def index():
    if (request.method == 'POST'):
        itemData = request.get_json()
        if (itemData['action'] == 'add'):
            # Initialize Item
            item = Item(itemData['id'], itemData['item_name'],
                        itemData['item_price'], itemData['item_amount'])
            cart.addItem(item)
            print(item.id)
            print(item.name)
            print(item.price)
            print(item.quantity)

        elif (itemData['action'] == 'update'):
            # Update Item
            item = Item(itemData['id'], itemData['item_name'],
                        itemData['item_price'], itemData['item_amount'])
            cart.updateItem(item)
            print(item.id)
            print(item.name)
            print(item.price)
            print(item.quantity)

        elif (itemData['action'] == 'discount'):
            discountRate = itemData['discountRate']
            cart.discount = int(discountRate)

        elif (itemData['action'] == 'tax'):
            taxRate = itemData['taxRate']
            cart.tax = int(taxRate)

        print(cart.subtotal)        
        cart.calculateTotal()
        print(cart.total)
        rtdict = {"netTotal": cart.subtotal, "grandTotal": cart.total}
        return(json.dumps(rtdict))

    if (request.method == "GET"):
        pass

    if (request.method == "DELETE"):
        cart.removeItem()

    return render_template("index.html")


####### Run Applications #######
if __name__ == '__main__':
    app.run(debug=True)
