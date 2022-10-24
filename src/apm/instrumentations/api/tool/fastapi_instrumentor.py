import opentelemetry.instrumentation.fastapi as otel_fastapi
from fastapi import FastAPI

from src.apm.instrumentations.api.tool.base_api_instrumentor import BaseAPIInstrumentor

class FastAPIInstrumentor(BaseAPIInstrumentor):
    
    def create_instrumentor(self):
        self._instrumentor = otel_fastapi.FastAPIInstrumentor()

    def instrument_app(self, app: FastAPI):
        self.instrumentor.instrument_app(app)