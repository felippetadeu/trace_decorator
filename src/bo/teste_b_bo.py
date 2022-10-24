from src.bo.teste_bo import Teste
from src.apm.trace.trace import trace


@trace
class B:
    def x(self):
        for i in range(10):
            Teste().d()
