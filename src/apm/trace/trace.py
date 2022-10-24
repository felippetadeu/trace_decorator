import builtins
import inspect

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
            
            python_environment = Configuration.get_environment()

            from src.apm.trace.tool.base_trace import BaseTrace
            trace_tool: BaseTrace = None
            if python_environment == "Prod":
                from src.apm.trace.tool.datadog import DataDog
                trace_tool = DataDog(name, attr)
            else:
                from src.apm.trace.tool.opentelemetry import OpenTelemetry
                trace_tool = OpenTelemetry(name, attr)

            return trace_tool.start_trace()
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
    #body = inspect.getsource(__getattribute__).split('\n')
    #fn = __create_fn("__getattribute__", body)
    setattr(cls, "__getattribute__", __getattribute__)

def __process_class(cls=None):
    __set_new_attribute(cls)
    return cls

def trace(cls=None):
    def wrap(cls):
        return __process_class(cls)

    return wrap(cls)