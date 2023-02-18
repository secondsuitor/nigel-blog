from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from nigel import app
from nigel.forms import LoginForm
from nigel.models import User

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'peter'}
    posts  = [
        {
            'author': {'username': 'peter'},
            'body': 'beautiful day'
        },
        {
            'author' : { 'username': 'tester'},
            'body': 'testing the waters'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/test')
def tester():
    user = {'username': 'tester'}
    return render_template('index.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))    
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)