from flask import Flask, render_template, request
import os

# app = Flask(__name__) # to make the app run without any
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)