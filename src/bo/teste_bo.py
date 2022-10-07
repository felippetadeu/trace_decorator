from src.apm.trace.trace import trace

@trace
class Teste:

    def a(self):
        print('a')

    def b(self):
        print('b')
        self.a()

    def d(self):
        self.c = 1
        print(self.c)
        self.b()