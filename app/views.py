from flask import render_template
from app import app
from .request import get_sources,get_article

@app.route('/')
def index():

    '''
    Display the page that returns the index page and its data
    '''
    source = get_sources('category')
    title = 'Home - Welcome to the News Recap online'
    message = 'ALL THAT HAPPENED'
    technology_source = get_sources('technology')
    sports_source = get_sources('sports')
    entertainment_source = get_sources('entertainment')
    return render_template('index.html',message = message, title = title, technology = technology_source, sports = sports_source, entertainment = entertainment_source)


@app.route('/news/<news_id>')
def news(news_id):

    '''
    Display news page that displays the news details and its data
    '''

    article = get_article(id)
    title = f'{article.content}'

    return render_template('news.html',id = news_id, title = title, article = article)