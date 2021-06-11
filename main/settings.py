class Settings:
    pass


class DevSettings(Settings):
    DEBUG = True
    # user:password@host:port/db
    SQLALCHEMY_DATABASE_URI = 'postgresql://root:toor@localhost:5432/orient'


class ProdSettings(Settings):
    SQLALCHEMY_DATABASE_URI = ''
