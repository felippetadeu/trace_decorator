from dataclasses import dataclass

from src.api.type import Type
from src.api.tool.fastapi import FastAPI

@dataclass
class API:
    
    type: str
    __api = None

    def __post_init__(self):
        if self.type == Type.FASTAPI.value:
            self.__api = FastAPI()

    @property
    def web_application(self):
        return self.__api.web_application

    def router(self):
        return self.__api.get_router()

    def include_router(self, router):
        self.web_application.include_router(router)