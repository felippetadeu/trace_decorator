import uvicorn
from fastapi import FastAPI, APIRouter

from src.configuration import Configuration
from src.cls_trace_decorator import trace

app = FastAPI(docs_url="/")
router = APIRouter()

@trace
class Teste:

    def a(self):
        print('a')

    def b(self):
        print('b')

    def d(self):
        self.c = 1
        print(self.c)

@router.get('/teste', tags=['Teste'])
def teste():
    x = Teste()
    x.a()
    x.b()
    x.d()
    
app.include_router(router)
if __name__=="__main__":
    Configuration.start_trace(__name__)
    uvicorn.run(app)