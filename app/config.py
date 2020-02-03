class Config:
    '''
    parent class for General configuration
    '''

    pass



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