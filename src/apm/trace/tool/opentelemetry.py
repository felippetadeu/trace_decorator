from opentelemetry import trace
from src.configuration import Configuration

from src.apm.configurations.tools.opentelemetry import OpenTelemetry as ConfigOpenTelemetry
from src.apm.trace.tool.base_trace import BaseTrace

class OpenTelemetry(BaseTrace):

    def __post_init__(self):
        if Configuration.provider is None:
            Configuration.start_apm()

    def start_trace(self):

        # Create a BatchSpanProcessor and add the exporter to it
        #span_processor = BatchSpanProcessor(jaeger_exporter)

        # add to the tracer
        #trace.get_tracer_provider().add_span_processor(span_processor)

        conf:ConfigOpenTelemetry = Configuration.apm_config.config
        with conf.tracer.start_as_current_span(self.name):
            return self.attr