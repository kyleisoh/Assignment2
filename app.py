####### Imports #######
import json
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from flask_wtf import FlaskForm
from forms import ItemForm

####### Setup/Config #######
app = Flask(__name__)
cors = CORS(app)
SECRET_KEY = 'SECRET_KEY'
app.config['SECRET_KEY'] = SECRET_KEY
api = Api(app)

####### Route Decorators #######


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
# Index Page
def index():
    form = ItemForm()
    if (request.method == "POST"):
        if form.validate_on_submit():
            item_name = form.item_name.data
        jsonData = request.get_json()
        print(jsonData)
        return {
            'name': jsonData
        }
    return render_template("index.html", form=form)


####### Run Applications #######
if __name__ == '__main__':
    app.run(debug=True)
