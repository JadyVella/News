from app import app
import urllib.request,json
from .models import source

Source = source.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]



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
        title = source_item.get('title')
        language = source_item.get('language')
        country = source_item.get('country')
        description = source_item.get('description')


        source_object = Source(id,name,title,language,country,description)
        source_results.append(source_object)


    return source_results



def get_article(id):
    get_article_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        article_object = None
        if article_details_response:
            id = article_details_response.get('id')
            author = article_details_response.get('author')
            url = article_details_response.get('url')
            image = article_details_response.get('urlToImage')
            date = article_details_response.get('publishedAt')
            content = article_details_response.get('content')

            article_object(self,id,author,url,image,date,content)

    return article_object



