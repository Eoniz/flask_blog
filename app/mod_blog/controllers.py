from flask import Blueprint, flash, redirect, render_template
from sqlalchemy import desc
from app.mod_blog.models import Blog
from app import app

mod_blog = Blueprint('blog', __name__, url_prefix='/')


@app.template_filter('format_date')
def format_date(date):
    """
    Format a datetime to "MONTH dd, YYYY at HH:MM:SS"
    params:
        date <datetime>:
            The given date to format
    returns:
        string:
            The formated datetime
    """

    # Declaring the months
    MONTHS = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December'
    ]
    
    date = str(date)  # Convert the date to string
    date_arr = date.split(' ')  # Split into two parts
    date_date = date_arr[0].split('-')  # Split the date
    date_hour = date_arr[1]

    date_year = date_date[0]
    
    # Get the litteraly month based on the number month
    date_month = MONTHS[int(date_date[1]) - 1]  
    
    date_day = date_date[2]

    return f'{date_month} {date_day}, {date_year} at {date_hour}'


@mod_blog.route('/')
@mod_blog.route('/page/<int:page>')
def index(page=1):
    """
    Return the index view with the given page.
    If no page given, the start page will be 1

    params:
        page <int>:
            The current page
    returns:
        render_template(blog/index.html)
    """
    offset = 50 * (page - 1)
    articles = Blog.query.order_by(desc(Blog.date_modified))\
        .offset(offset).limit(20)

    return render_template('blog/index.html', articles=articles)
