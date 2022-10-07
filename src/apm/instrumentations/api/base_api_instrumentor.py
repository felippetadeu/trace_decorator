from dataclasses import dataclass

@dataclass
class BaseAPIInstrumentor:

    _instrumentor = None

    def instrument_app(self):
        raise NotImplementedError()

    def create_instrumentor(self):
        raise NotImplementedError()

    @property
    def instrumentor(self):
        if self._instrumentor is None:
            self.create_instrumentor()

        return self._instrumentor