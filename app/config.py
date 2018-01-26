class Config:
    '''
    General configuration parent class
    '''
    pass

class ProdConfig(Config):
'''
Production configuration child class
Args:
    Config: The parent configuration class with general configuration settings
'''
pass

class DevConfig(Config):
    '''
    Development configuration class with general configuration settings
    '''

    DEBUG = True
