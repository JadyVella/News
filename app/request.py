from app import app
import urllib.request,json
from .models import source,article

Source = source.Source
Article = article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

# article_base_url = app.config["ARTICLE_BASE_URL"]
articles_url = app.config["ARTICLE_BASE_URL"]

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''

    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)


        source_results = None


        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_sources(source_results_list)


    return source_results



def process_sources(source_list):
    '''
    Function that processes the source result and transform them to a list of Objects
    '''

    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        language = source_item.get('language')
        country = source_item.get('country')
        description = source_item.get('description')


        source_object = Source(id,name,language,country,description)
        source_results.append(source_object)


    return source_results



def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''

    get_articles_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)


        article_results = None


        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)


    return article_results



def process_articles(articles_list):

    article_list = []
    for article_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedAt')
        content = article_item.get('content')
        title = article_item.get('title')
        
        if image:
            article_results = Article(id,author,url,image,date,content,title)
            article_list.append(article_results)


    return article_list