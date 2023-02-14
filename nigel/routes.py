from flask import render_template, flash, redirect, url_for
from nigel import app
from nigel.forms import LoginForm

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
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remeber_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)