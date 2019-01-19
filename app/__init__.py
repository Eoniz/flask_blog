# Imports
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# App
app = Flask(__name__)

# Config
app.config.from_object('config')

# Database
db = SQLAlchemy(app)

# Basic errors
@app.errorhandler(404)
def not_found():
    return render_template('404.html'), 404