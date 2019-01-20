# Imports
from flask import Flask, render_template, session, redirect, request
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


@app.before_request
def logged_in_required():
    """
    Decorator middleware for redirect user when he's not logged in
    """
    valid = 'user_id' in session

    if(request.endpoint and 'static' not in request.endpoint and not
        valid and not getattr(
            app.view_functions[request.endpoint], 'is_public', False)):
        return redirect('/auth/login')
    

def public_endpoint(f):
    f.is_public = True
    return f


def route(rule, **options):
    """
    Decorator for creating 2 routes.
    First is /route ; Second is /route/
    
    :param rule: The given path
    :param options: The options
    """
    def decorator(f):
        if len(rule) > 1:
            decorator = app.route(rule + '/', **options)
            decorator(f)
        decorator = app.route(rule, **options)
        decorator(f)

        return f

    return decorator


from app.mod_auth.controllers import mod_auth
app.register_blueprint(mod_auth)

from app.mod_blog.controllers import mod_blog
app.register_blueprint(mod_blog)

db.create_all()
