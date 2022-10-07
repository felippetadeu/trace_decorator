from dataclasses import dataclass
from ddtrace import patch

from src.apm.configurations.tools.base_configuration import BaseConfiguration

@dataclass
class DataDog(BaseConfiguration):

    def setUp(self, name: str):
        patch(fastapi=True)