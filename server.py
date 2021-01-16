#app.py
from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, World2!'
@app.route('/say-my-name')
def hello_world():
    return 'Hello, ' + request.args.get('name')
