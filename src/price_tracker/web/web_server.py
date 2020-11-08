import os
import webbrowser
from threading import Timer
from flask import Flask, render_template, json, request


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


@app.route('/config', methods=['PUT', 'DELETE'])
def config_handler():
    if request.method == 'PUT':
        request_data = request.get_json()
        with open(CONFIG_PATH, 'w') as config_file:
            json.dump(request_data, config_file)
        return {'status': 200}
    elif request.method == 'DELETE':
        os.remove(CONFIG_PATH)
        return {'status': 200}


@app.route('/products', methods=['PUT', 'DELETE'])
def products_handler():
    if request.method == 'PUT':
        request_data = request.get_json()
        for req in request_data:
            req['warn_price'] = float(req['warn_price'])
        with open(PRODUCTS_PATH, 'w') as products_file:
            json.dump(request_data, products_file)
        return {'status': 200}
    elif request.method == 'DELETE':
        os.remove(PRODUCTS_PATH)
        return {'status': 200}


def open_browser():
    webbrowser.open('http://127.0.0.1:5051/', new=2, autoraise=True)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return {'status': 200}


def run():
    Timer(1, open_browser).start()
    app.run(debug=False, port=5051)
