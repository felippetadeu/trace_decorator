from dataclasses import dataclass

@dataclass
class BaseMetric:

    name: str

    def start(self):
        raise NotImplementedError()