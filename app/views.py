from flask import render_template
from app import app
from .request import get_sources,get_articles
from .models import source, article

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
    return render_template('index.html', title = title,source = source, technology = technology_source, sports = sports_source, entertainment = entertainment_source)


@app.route('/source/<id>')
def article(id):

    '''
    Display article page that displays the article details and its data
    '''

    articles = get_articles(id)

    return render_template('source.html', id = id, article = articles)