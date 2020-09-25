import os


BASE_DIR=os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """Base Flask configuration class"""
    DEBUG=False
    TESTING=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False


class DevConfig(BaseConfig):
    """Development Configuration class

    Args:
        BaseConfig (class): Super configuration class to inherit from
    """
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(BASE_DIR, 'dev_db.sqlite')}"


class TestingConfig(BaseConfig):
    """Testing configuration class

    Args:
        BaseConfig (class): Super configuration class to inherit from
    """
    DEBUG=True
    TESTING=True
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(BASE_DIR, 'testing_db.sqlite')}"



class ProdConfig(BaseConfig):
    """[summary]

    Args:
        BaseConfig (class): Super configuration class to inherit from
    """
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(BASE_DIR, 'production_db.sqlite')}"




config_factory = {'default': DevConfig, 'development': DevConfig, 'testing': TestingConfig, 'production': ProdConfig}
