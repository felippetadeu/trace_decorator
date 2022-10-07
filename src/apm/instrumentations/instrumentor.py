from dataclasses import dataclass
from typing import Any

from src.apm.instrumentations.api.api_instrumentor import APIInstrumentor

@dataclass
class Instrumentor:
    
    app: Any
    type: str
    api_instrumentor: APIInstrumentor = None

    def __post_init__(self):
        self.api_instrumentor = APIInstrumentor(self.type)
        self.api_instrumentor.instrumentor.instrument_app(self.app)