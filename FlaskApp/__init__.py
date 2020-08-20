from flask import Flask, render_template
import jinja2
import os
import sys


app = Flask(__name__)
jinja_environment = jinja2.Environment(loader= jinja2.FileSystemLoader('templates'))
cwd = os.getcwd()

@app.route('/')
def homepage():
    return render_template('main.html')

if __name__ == "__main__":
    app.run()
