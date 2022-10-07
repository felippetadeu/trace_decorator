from dataclasses import dataclass
from fastapi import FastAPI as BaseFastAPI, APIRouter

@dataclass
class FastAPI:
    
    web_application = None
    __router: APIRouter = None

    def __post_init__(self):
        self.web_application = BaseFastAPI()

    def get_router(self):
        if self.__router is None:
            self.__router = APIRouter()

        return self.__router