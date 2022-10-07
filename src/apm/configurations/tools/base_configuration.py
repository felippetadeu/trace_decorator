from dataclasses import dataclass
from typing import Any

@dataclass
class BaseConfiguration:
    tracer: Any = None
    provider: Any = None
    span_processor: Any = None

    def setUp(self, name: str):
        raise NotImplementedError()