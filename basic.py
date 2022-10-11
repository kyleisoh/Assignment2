from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'csc301'


class CartForm(FlaskForm):

    cart = StringField("What item is in the cart?")
    submit = SubmitField('Ready to checkout?')


@app.route('/', methods=['GET', 'POST'])
def index():
    cart = False
    form = CartForm()

    if form.validate_on_submit():
        cart = form.cart.data
        form.cart.date = ''
    return render_template('index.html', form=form, cart=cart)


class Cart(Resource):

    def get(self):
        return {'apple': '1'}


api.add_resource(Cart, '/')

if __name__ == '__main__':
    app.run(debug=True)
