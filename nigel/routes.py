from flask import render_template
from nigel import app

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