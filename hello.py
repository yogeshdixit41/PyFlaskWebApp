import os
from flask import Flask, jsonify, render_template, request
import flask

app = Flask(__name__)

@app.route('/')
def hello():
    return flask.render_template('main_page.html')

@app.route('/yogesh')
def hello_yogesh():
    return jsonify(name='Yogesh D')

@app.route('/naman')
def hello_naman():
    return jsonify(name='Naman')

@app.route('/khushbu')
def hello_khushbu():
    return 'Khushbu'

@app.route('/nathan')
def hello_nate():
    return 'Nate'

@app.route('/Anumeha')
def hello_anu():
    return 'Anu'

if __name__ == '__main__':
    app.debug=True
    app.run()

