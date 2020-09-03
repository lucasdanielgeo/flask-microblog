from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Lucas'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beatiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avangers movie was so cool!'
        }
    ]
    
    return render_template('index.html', title='Home', user=user, posts=posts)