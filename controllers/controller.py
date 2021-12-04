from app import app
from flask import render_template, request
from models.shopping_list import shopping_list, add_new_item, Item

@app.route('/list')
def index():
    return render_template('index.html', title='All items', shopping_list=shopping_list)

@app.route('/list', methods = ['POST'])
def add_item():
    name = request.form['name']
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])
    if "bought" in request.form:
        bought = True
    else:
        bought = False
    new_item = Item(name, price, quantity, bought)
    shopping_list.append(new_item)
    return render_template('index.html', title='All items', shopping_list=shopping_list)

    