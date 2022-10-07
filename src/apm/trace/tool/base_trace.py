from dataclasses import dataclass
from typing import Any

@dataclass
class BaseTrace:
    
    name: str
    attr: Any

    def start_trace(self):
        raise NotImplementedError()