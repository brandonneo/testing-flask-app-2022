# from flask import Blueprint
from flask import render_template;
from app import app

@app.route('/')
def index():
    return render_template('index.html')
    #return "test"
