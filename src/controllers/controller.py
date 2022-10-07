from src.configuration import Configuration
from src.bo.teste_bo import Teste

router = Configuration.app.router()


@router.get('/a', tags=['Teste'])
def teste():
    x = Teste()
    x.a()

@router.get('/b', tags=['Teste'])
def teste():
    x = Teste()
    x.b()

@router.get('/c', tags=['Teste'])
def teste():
    x = Teste()
    x.c()