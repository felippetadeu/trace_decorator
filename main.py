from src.trace_decorator import trace

@trace
class Teste:

    def a(self):
        print('a')

    def b(self):
        print('b')

    def d(self):
        self.c = 1
        print(self.c)


x = Teste()
x.a()
x.b()
x.d()