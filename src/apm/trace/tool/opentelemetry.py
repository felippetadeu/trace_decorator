from opentelemetry import trace
from src.configuration import Configuration

from src.apm.configurations.tools.opentelemetry import OpenTelemetry as ConfigOpenTelemetry
from src.apm.trace.tool.base_trace import BaseTrace

class OpenTelemetry(BaseTrace):

    def __post_init__(self):
        if Configuration.provider is None:
            Configuration.start_apm()

    def start_trace(self):
        conf:ConfigOpenTelemetry = Configuration.apm_config.config
        with conf.tracer.start_as_current_span(self.name):
            return self.attr