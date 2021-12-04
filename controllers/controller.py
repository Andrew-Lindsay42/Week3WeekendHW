from app import app
from flask import render_template
from models.shopping_list import shopping_list
from models.Item import Item

@app.route('/list')
def index():
    return render_template('index.html', title='All items', shopping_list=shopping_list)
