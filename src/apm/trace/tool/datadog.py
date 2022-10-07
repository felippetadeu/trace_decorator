from typing import Any
from opentelemetry import trace
from ddtrace import tracer as dd_tracer
from src.configuration import Configuration

from src.apm.trace.tool.base_trace import BaseTrace

class DataDog(BaseTrace):

    def __post_init__(self):
        self.trace_link = trace.Link(trace.get_current_span().get_span_context()) if getattr(self, 'trace_link') is None else None
        
        try:
            self.span_name = self.attr.__module__
        except:
            self.span_name = self.name
        if self.span_name is None:
            self.span_name = ''
    
    def __trace_dd(self, new_span):
        trace_link_data_dog = getattr(self, 'trace_link_data_dog')
        with dd_tracer.start_span(self.span_name+'.'+ self.name, child_of=trace_link_data_dog) as trace_data_dog:
            setattr(self, 'trace_link_data_dog', trace_data_dog)       
            setattr(self, 'trace_link', new_span)       
            return self.attr

    def start_trace(self) -> Any:

        if self.trace_link is not None:
            with Configuration.tracer.start_as_current_span(self.span_name+'.'+ self.attr.__name__, links=[self.trace_link]) as new_span:
                return self.__trace_dd(new_span)
        else:
            context = trace.set_span_in_context(getattr(self, 'trace_link'))
            new_span = Configuration.tracer.start_span(self.span_name+'.'+ self.attr.__name__, context=context)
            try:
                with trace.use_span(new_span):
                    return self.__trace_dd(new_span)
            finally:
                new_span.end()