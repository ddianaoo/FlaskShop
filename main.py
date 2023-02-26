from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import AddItem
from cloudipsp import Api, Checkout


app = Flask(__name__)
SECRET_KEY = 'juicy-pussy-money-money-pussy-juicy'
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.title


@app.route('/create', methods=["POST", "GET"])
def create():
    form = AddItem()
    if form.validate_on_submit():
        try:
            item = Item(title=form.title.data, price=form.price.data, text=form.text.data)
            db.session.add(item)
            db.session.flush()
            db.session.commit()
            return redirect('/')
        except:
            db.session.rollback()
            print("Ошибка добавления в БД")

    return render_template('create.html', title='Create new product', form=form)


@app.route('/product/<int:id>')
def get_product(id):
    try:
        product = Item.query.get(id)
    except:
        print("Ошибка получения  из БД")
        return redirect('/')

    return render_template('get_product.html', product=product)


@app.route('/')
def index():
    products = []
    try:
        products = Item.query.order_by(Item.price).all()
    except:
        print("Ошибка получения  из БД")

    return render_template('get_products.html', title='Products', products=products)


@app.route('/about')
def about():
    return render_template('about.html', title='The details')


@app.route('/product/<int:id>/buy')
def buy(id):
    return f'buy buy buy {id}'


if __name__ == '__main__':
    app.run(debug=True)