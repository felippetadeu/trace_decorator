import configparser
import os

from src.api.api import API
from src.apm.instrumentations.instrumentor import Instrumentor
from src.apm.metrics.metrics import Metrics
from src.apm.configurations.configuration import Configuration as APMConfiguration

from src.enums.sections import Sections as SectionsEnum

class Configuration:

    app:API = None
    apm_config: APMConfiguration = None
    instrumentor: Instrumentor = None
    
    settings: configparser.ConfigParser = None

    @staticmethod
    def start_app() -> API:
        app = API(Configuration.get_settings(SectionsEnum.API.value, 'type'))
        Configuration.app = app
        import src.controllers.controller
        
        app.include_router(app.router())
        return app

    @staticmethod
    def start_apm(name: str):
        env = Configuration.get_environment()
        Configuration.apm_config = APMConfiguration(env)
        Configuration.metrics = Metrics(env, name)
        Configuration.instrumentor = Instrumentor(Configuration.app.web_application, Configuration.get_settings(SectionsEnum.API.value, 'type'))

    @staticmethod
    def get_environment(key: str = "PYTHON_ENVIROMENT") -> str:
        return os.getenv(key)

    @staticmethod
    def load_settings(reload: bool = False):
        if Configuration.settings is None or reload:
            env = Configuration.get_environment()
            if env is not None:
                env = f".{env}"
            else:
                env = ''

            path = os.path.join(os.getcwd(), "src", f'settings{env}.ini')
            Configuration.settings = configparser.ConfigParser()
            Configuration.settings.read(path)

    @staticmethod
    def get_settings(section: str, key: str):
        if Configuration.settings is None:
            Configuration.load_settings()
        return Configuration.settings.get(section, key)