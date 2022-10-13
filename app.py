####### Imports #######
import json
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
from cart import Cart


####### Setup/Config #######
app = Flask(__name__)
CORS(app)
api = Api(app)

####### Route Decorators #######


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
# Index Page
def index():
    if request.method == "POST":
        # parse as JSON
        jsonData = request.get_json()
        print(jsonData)
        return {
            'name': jsonData
        }
    return render_template("index.html")


####### Run Applications #######
if __name__ == '__main__':
    app.run(debug=True)
