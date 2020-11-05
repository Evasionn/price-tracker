import os

from flask import Flask, render_template, json

from price_tracker.constants import CONFIG_PATH, PRODUCTS_PATH

app = Flask(__name__)


@app.route('/')
def index():
    config = {}
    products = []
    try:
        with open(CONFIG_PATH) as json_file:
            config = json.load(json_file)
        with open(PRODUCTS_PATH) as json_file:
            products = json.load(json_file)
    except FileNotFoundError:
        pass
    return render_template('index.html', config=config, products=products)


if __name__ == '__main__':
    app.run(debug=True)
