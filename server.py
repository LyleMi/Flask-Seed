#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session, flash

app = Flask(__name__)
app.secret_key = 'my_secret_key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/get")
def getAction():
    param = request.args.get("param", "0")
    return param


@app.route("/post", methods=['POST'])
def postAction():
    data = request.form["data"]
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
