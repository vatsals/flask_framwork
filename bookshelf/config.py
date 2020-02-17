class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SECRET_KEY = "Random"
    SECURITY_PASSWORD_SALT = "Password"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    ENV = "dev"
    SQLALCHEMY_DATABASE_URI = "sqlite:///main_app.db"
    SECRET_KEY = "Random"


class StagingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    ENV = "staging"
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SECRET_KEY = "Random"


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    ENV = "prod"
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SECRET_KEY = "Random"


config = {
    "dev": "bookshelf.config.DevelopmentConfig",
    "staging": "bookshelf.config.StagingConfig",
    "prod": "bookshelf.config.ProductionConfig",
    "default": "bookshelf.config.DevelopmentConfig",
}


def configure_app(app):
    config_name = 'default'
    app.config.from_object(config[config_name])
    # app.config.from_pyfile("config.cfg", silent=True)
