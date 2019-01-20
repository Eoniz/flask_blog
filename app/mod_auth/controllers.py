from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.mod_auth.forms import LoginForm
from app.mod_auth.models import User

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()

        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            
            return redirect('/')

        flash(f'Wrong email or password', 'danger')
    else:
        flash(f"Email and/or password is not correct", "danger")

    return render_template('auth/signin.html', form=form)


@mod_auth.route('/logout')
def logout():
    session.pop('user_id', None)

    return redirect('/')

