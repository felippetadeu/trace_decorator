from dataclasses import dataclass
from typing import Any

from src.apm.metrics.tool.base_metric import BaseMetric
from src.apm.metrics.tool.opentelemetry import OpenTelemetry
from src.apm.metrics.tool.datadog import DataDog

@dataclass
class Metrics:
    env: str
    name: str
    meter: Any = None
    tool: BaseMetric = None

    def __post_init__(self):
        if self.env == "Prod":
            self.tool = DataDog(self.name)
        else:
            self.tool = OpenTelemetry(self.name)

        self.meter = self.tool.start()