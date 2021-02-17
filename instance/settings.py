class Settings:
    pass

class DevSettings(Settings):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ''

class ProdSettings(Settings):
    SQLALCHEMY_DATABASE_URI = ''