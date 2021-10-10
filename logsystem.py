import os 
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/login.html')
def index():
    return redirect(url_for('login.html'))
    