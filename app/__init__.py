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
def not_found(error):
    return render_template('404.html'), 404


from app.mod_auth.controllers import mod_auth
app.register_blueprint(mod_auth)

db.create_all()
