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


        source_result = None


        if get_sources_response['results']:
            source_results_list = get_sources_response['results']
            source_result = process_results(source_results_list)


    return source_result



def process_results(source_list):
    '''
    Function that processes the source result and transform them to a list of Objects
    '''

    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        language = source_item.get('language')
        country = source_item.get('country')


        source_object = Source(id,name,description,language,country)
        source_results.append(source_object)


    return source_results



def get_source(id):
    get_source_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_source_details_url) as url:
        source_details_data = url.read()
        source_details_response = json.loads(source_details_data)

        source_object = None
        if source_details_response:
            id = source_details_response.get('id')
            


