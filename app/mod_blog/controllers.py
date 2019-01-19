from flask import Blueprint, flash, redirect, render_template

mod_blog = Blueprint('blog', __name__, url_prefix='/')


@mod_blog.route('/')
def index():
    return render_template('blog/index.html')
