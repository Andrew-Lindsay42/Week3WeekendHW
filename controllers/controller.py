from app import app
from flask import render_template, request, redirect
from models.shopping_list import shopping_list, add_new_item, total_cost, Item

@app.route('/list')
def index():
    return render_template('index.html', title='All items', shopping_list=shopping_list, total_cost = total_cost(shopping_list))

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
    add_new_item(new_item)
    return render_template('index.html', title='All items', shopping_list=shopping_list)

@app.route('/list/bought', methods = ['POST'])
def show_bought_items():
    return render_template('bought.html', title='Bought items', shopping_list=shopping_list)

@app.route('/list/unbought', methods = ['POST'])
def show_unbought_items():
    return render_template('unbought.html', title='Unbought items', shopping_list=shopping_list)

@app.route('/list/show_all', methods = ['POST'])
def show_all():
    return redirect ('/list')