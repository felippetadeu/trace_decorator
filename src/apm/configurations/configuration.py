from dataclasses import dataclass

from src.apm.configurations.tools.base_configuration import BaseConfiguration
from src.apm.configurations.tools.opentelemetry import OpenTelemetry

@dataclass
class Configuration:
    
    env: str
    config: BaseConfiguration = None

    def __post_init__(self):
        if self.env == "Prod":
            pass
        else:
            self.config = OpenTelemetry()
            self.config.setUp(__name__)