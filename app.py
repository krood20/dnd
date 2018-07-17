from flask import Flask, render_template, request, redirect, url_for, g, flash

STATIC_FOLDER = 'static'

app = Flask(__name__, static_folder=STATIC_FOLDER)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/dice')
def dicepage():
    return render_template('dice.html')

@app.route('/character_builder')
def characterbuilder():
    return render_template('character_builder.html')
