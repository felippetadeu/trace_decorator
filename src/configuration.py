import os
from opentelemetry import trace

class Configuration:

    tracer = None

    @staticmethod
    def start_trace(name: str):
        Configuration.tracer = trace.get_tracer(name)
        if Configuration.get_environment() == "Prod":
            from ddtrace import patch
            patch(fastapi=True)

    @staticmethod
    def get_environment(key: str = "PYTHON_ENVIROMENT") -> str:
        return os.getenv(key)