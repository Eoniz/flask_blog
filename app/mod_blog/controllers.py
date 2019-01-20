from flask import Blueprint, flash, request, redirect, render_template
from sqlalchemy import desc
from app.mod_blog.models import Blog
from app import app, route
from app.mod_blog.forms import WriteArticle

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


@route('/')
@route('/page/<int:page>')
@route('/page/<int:page>/limit/<int:limit>')
def index(page=1, limit=10):
    """
    Return the index view with the given page.
    If no page given, the start page will be 1

    params:
        page <int>:
            The current page
        limit <int>:
            The number of articles per page
    returns:
        render_template(blog/index.html)
    """

    offset = limit * (page - 1)
    articles = Blog.query.order_by(desc(Blog.date_modified))\
        .offset(offset).limit(limit)

    return render_template('blog/index.html', articles=articles)


@mod_blog.route('/write', methods=['GET', 'POST'])
@mod_blog.route('/write/', methods=['GET', 'POST'])
def write():
    form = WriteArticle(request.form)

    if form.validate_on_submit():
        blog = Blog(form.title.data, form.content.data)
        blog.save()

        return redirect('/')

    return render_template('blog/write.html', form=form)


@route('/delete/<int:id>')
def delete_by_id(id):
    article = Blog.query.filter_by(id=id).first()

    if article is not None:
        article.remove()

    return redirect('/')

