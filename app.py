import os

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
import time

from flask import Flask, render_template, request, redirect, url_for, jsonify
import numpy as np
import json

import random
import string

app = Flask(__name__)

def picked_up():
    messages = [
        "こんにちは、あなたの名前を入力してください",
        "やあ！お名前は何ですか？",
        "あなたの名前を教えてね"
    ]
    return np.random.choice(messages)

@app.route('/')
def index():
    title = "ようこそ"
    message = picked_up()
    return render_template('index.html',
                           message=message, title=title)

@app.route('/post', methods=['GET', 'POST'])
def post():
    title = "こんにちは"
    if request.method == 'POST':
        name = request.form['name']
        return render_template('post.html',
                               name=name, title=title)
    else:
        return redirect(url_for('index'))

@app.route('/display', methods=['GET', 'POST'])
def diplay():
    title = "You can see your graph"
    if request.method == 'POST':
        labels = ["January","February","March","April","May","June","July","August"]
        values = [10,9,8,7,6,4,7,8]
        return_data = {
            "labels":labels,
            "values":values
        }
        print("r", return_data)
        return render_template('graph.html', title=title, values=values, labels=labels)
        #return render_template('graph.html', jsonify(ResultSet=json.dumps(return_data)))
    else:
        return "Error"

@app.route('/calender', methods=['GET', 'POST'])
def calender():
    if request.method == 'POST':
        colored_day = [
        "2017-06-02",
        "2017-06-08"
        ]
        labels = ["January","February","March","April","May","June","July","August"]
        values = [10,9,8,7,6,4,7,8]
        return render_template('calender.html',
            title="calender",
            colored_day=colored_day,
            labels=labels,
            values=values)
    else:
        return "Error"

@app.route('/change', methods=['GET', 'POST'])
def change():
    text = request.json['text']
    if "ping" in text:
        return_data = {"result":"pong"}
        return jsonify(ResultSet=json.dumps(return_data))
    lower_text = text.lower()
    return_data = {"result":lower_text}
    return jsonify(ResultSet=json.dumps(return_data))

@app.route("/aaa/<i>")
def t(i):
    return i

@app.route('/test', methods=["GET", "POST"])
def test():
    return_data = {
    "title": "Error",
    "message": "Error",
    "hogehoge": "Error"
    }
    rand_a = [random.randint(1, 8) for n in range(26)]
    hoge = "abcdefghijklmnopqrstu"
    rand_b = [random.choice(hoge) + "xausia" for n in range(26)]

    print(rand_b)
    a_arr = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in rand_a:
        a_arr[i - 1] += 1

    print(a_arr)

    if request.method == "POST":
        return_data = {
        "title": "Hello",
        "message": "message",
        "hogehoge": "hogehoge",
        "a":a_arr
        }

        dates = ["2017-06-15", "2017-06-16", "2017-06-18"]
        reasons = ["", "ppo", "pupp"]

        cal_data = {
            "date_answer" : [dates, reasons]
        }
    return render_template("test.html",
        title="What",
        message="Wow",
        b=rand_b,
        ResultSet=json.dumps(return_data),
        CalSet=json.dumps(cal_data)
        )

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == '__main__':
    #app.debug = True # デバッグモード有効化
    #port = int(os.environ.get('PORT', 5000))
    #app.run(port=port)
    app.run()
