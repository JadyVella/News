from flask import render_template
from app import app

@app.route('/')
def index():

    '''
    Display the page that returns the index page and its data
    '''

    title = 'Home - Welcome to the News Recap online'
    message = 'Welcome to News Recap'
    return render_template('index.html',message = message, title = title)


@app.route('/news/<news_id>')
def movie(news_id):

    '''
    Display news page that displays the news details and its data
    '''

    return render_template('news.html',id = news_id)