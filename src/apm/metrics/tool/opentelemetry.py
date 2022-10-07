from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
)
from src.apm.metrics.tool.base_metric import BaseMetric

class OpenTelemetry(BaseMetric):
    
    def start(self):
        metric_reader = PeriodicExportingMetricReader(ConsoleMetricExporter())
        provider = MeterProvider(metric_readers=[metric_reader])

        # Sets the global default meter provider
        metrics.set_meter_provider(provider)

        # Creates a meter from the global meter provider
        self.meter = metrics.get_meter(__name__)
        return self.meter