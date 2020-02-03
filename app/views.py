from flask import render_template
from app import app

@app.route('/')
def index():

    '''
    Display the page that returns the index page and its data
    '''

    message = 'Welcome to News Recap'
    return render_template('index.html',message = message)


@app.route('/news/<news_id>')
def movie(news_id):