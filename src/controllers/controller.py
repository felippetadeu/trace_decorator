from src.configuration import Configuration
from src.bo.teste_bo import Teste

router = Configuration.app.router()


@router.get('/a', tags=['Teste'])
def a():
    x = Teste()
    x.a()

@router.get('/b', tags=['Teste'])
def b():
    x = Teste()
    x.b()

@router.get('/c', tags=['Teste'])
def c():
    x = Teste()
    x.d()

@router.get('/d', tags=['Teste'])
def d():
    x = Teste()
    x.c()

@router.get('/e', tags=['Teste'])
def e():
    x = B()
    x.x()