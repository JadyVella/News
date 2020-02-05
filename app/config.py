import os

class Config:
    '''
    parent class for General configuration
    '''

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=cb11bc0bcb56433db9af73d42788be5d'
    ARTICLE_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}