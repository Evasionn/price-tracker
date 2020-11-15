import os
import smtplib
import webbrowser
from threading import Timer

from flask import Flask, json, render_template, request, jsonify
from price_tracker.constants import CONFIG_PATH, PRODUCTS_PATH
from exceptions import LoginAttemptFailed

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


@app.route('/check-login', methods=['POST'])
def check_login():
    request_data = request.get_json()
    print(request_data)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(request_data['email'],
                     request_data['password'])
    except smtplib.SMTPAuthenticationError:
        raise LoginAttemptFailed
    finally:
        server.quit()
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


@app.errorhandler(LoginAttemptFailed)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def run():
    Timer(1, open_browser).start()
    app.run(debug=False, port=5051)
