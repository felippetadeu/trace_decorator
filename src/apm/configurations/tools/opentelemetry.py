from dataclasses import dataclass
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from src.apm.configurations.tools.base_configuration import BaseConfiguration

@dataclass
class OpenTelemetry(BaseConfiguration):
    
    def setUp(self, name: str):
        self.tracer = trace.get_tracer(name)
        self.provider = TracerProvider(
            resource=Resource.create({SERVICE_NAME: "my-helloworld-service"})
        )
        trace.set_tracer_provider(self.provider)

        # create a JaegerExporter
        jaeger_exporter = JaegerExporter(
            # configure agent
            agent_host_name='localhost',
            agent_port=6831,
        )
        
        span_processor = BatchSpanProcessor(jaeger_exporter)
        trace.get_tracer_provider().add_span_processor(span_processor)