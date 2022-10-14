####### Imports #######
import json
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api

####### Setup/Config #######
app = Flask(__name__)
cors = CORS(app)
SECRET_KEY = 'SECRET_KEY'
app.config['SECRET_KEY'] = SECRET_KEY
api = Api(app)

####### Route Decorators #######
@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def index():
    #form = ItemForm()
    if (request.method == "POST"):
        jsonData = request.get_json()
        print(jsonData)
        return {
            'name': jsonData
        }
    return render_template("index.html")


####### Run Applications #######
if __name__ == '__main__':
    app.run(debug=True)
