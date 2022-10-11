# Third Party Imports
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'csc301'


class ItemForm(FlaskForm):

    item = StringField("What item is in the cart?")
    submit = SubmitField('Ready to checkout?')


@app.route('/', methods=['GET', 'POST'])
def index():
    item = False
    form = ItemForm()

    if form.validate_on_submit():
        item = form.item.data
        form.item.date = ''
    return render_template('index.html', form=form, item=item)


class Item(Resource):

    def get(self):
        return {'apple': '1'}


api.add_resource(Item, '/')

if __name__ == '__main__':
    app.run(debug=True)
