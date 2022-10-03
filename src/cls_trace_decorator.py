import builtins
import inspect

from opentelemetry.trace import set_span_in_context
from ddtrace import tracer as dd_tracer

from src.configuration import Configuration

LIST_OF_DEFAULT_METHODS = [
    '__annotations__', 
    '__weakref__', 
    '__dict__', 
    '__module__'
]

def __getattribute__(self, name: str):
        
        attr = object.__getattribute__(self, name)
        if name == "__class__":
            return object.__getattribute__(self, name)
        class_methods = set(dir(self.__class__)) - set(dir(object)) - set(LIST_OF_DEFAULT_METHODS)
        if name in class_methods:
            print(f'fui chamado {name}')

            def trace_dd():

                trace_link_data_dog = getattr(self, 'trace_link_data_dog')
                with dd_tracer.start_span(span_name+'.'+name, child_of=trace_link_data_dog) as trace_data_dog:
                    setattr(self, 'trace_link_data_dog', trace_data_dog)       
                    setattr(self, 'trace_link', new_span)       
                    return attr

            python_environment = Configuration.get_environment()
            if python_environment == "Prod":
                from opentelemetry import trace                    
                trace_link = trace.Link(trace.get_current_span().get_span_context()) if getattr(self, 'trace_link') is None else None
                
                try:
                    span_name = attr.__module__
                except:
                    span_name = __name__
                if span_name is None:
                    span_name = ''

                if trace_link is not None:
                    with Configuration.tracer.start_as_current_span(span_name+'.'+attr.__name__, links=[trace_link]) as new_span:
                        trace_dd()
                else:
                    context = set_span_in_context(getattr(self, 'trace_link'))
                    new_span = Configuration.tracer.start_span(span_name+'.'+attr.__name__, context=context)
                    try:
                        with trace.use_span(new_span):
                            trace_dd()
                    finally:
                        new_span.end()

        return attr

def __create_fn(name, body, *, globals=None, locals=None):
    if locals is None:
        locals = {}
    if 'BUILTINS' not in locals:
        locals['BUILTINS'] = builtins
    
    body = '\n'.join(f'  {b}' for b in body)

    local_vars = ', '.join(locals.keys())
    txt = f"def __create_fn__({local_vars}):\n{body}\n  return  {name}"
    ns = {}
    exec(txt, globals, ns)
    return ns['__create_fn__'](**locals)

def __set_new_attribute(cls=None):
    body = inspect.getsource(__getattribute__).split('\n')
    fn = __create_fn("__getattribute__", body)
    setattr(cls, "__getattribute__", fn)

def __process_class(cls=None):
    __set_new_attribute(cls)
    return cls

def trace(cls=None):
    def wrap(cls):
        return __process_class(cls)

    return wrap(cls)