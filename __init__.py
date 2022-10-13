# Third Party Imports
from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_wtf import FlaskForm  # from wtforms import StringField, SubmitField

# Setup/Config
app = Flask(__name__)
api = Api(app)

# Route Decorators


@app.route('/', methods=['GET', 'POST'])
# Index Page
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
