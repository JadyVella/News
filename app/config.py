class Config:
    '''
    parent class for General configuration
    '''

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?{}apiKey={}'



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