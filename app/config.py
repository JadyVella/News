class Config:
    '''
    parent class for General configuration
    '''

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=cb11bc0bcb56433db9af73d42788be5d'



class ProdConfig(Config):
    '''
    A child class for production configuration
    '''

    pass


class DevConfig(Config):
    '''
    A child class for Development configuration
    '''

    DEBUG = True