from dataclasses import dataclass
from src.apm.instrumentations.api.tool.base_api_instrumentor import BaseAPIInstrumentor
from src.apm.instrumentations.api.tool.fastapi_instrumentor import FastAPIInstrumentor
from src.api.type import Type as APITypesEnum

@dataclass
class APIInstrumentor:
    
    type: str
    instrumentor: BaseAPIInstrumentor = None


    def __post_init__(self):
        if self.type == APITypesEnum.FASTAPI.value:
            self.instrumentor = FastAPIInstrumentor()