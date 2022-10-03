import builtins

LIST_OF_DEFAULT_METHODS = [
    '__annotations__', 
    '__weakref__', 
    '__dict__', 
    '__module__'
]

def __create_fn(name, body, *, globals=None, locals=None):
    # Note that we mutate locals when exec() is called.  Caller
    # beware!  The only callers are internal to this module, so no
    # worries about external callers.
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
    class_methods = set(dir(cls)) - set(dir(object)) - set(LIST_OF_DEFAULT_METHODS)
    list_of_user_defineds = "['" + "','".join(class_methods) + "']"
    body = ["def __getattribute__(self, name: str):"]
    body.append("  import inspect")
    body.append(f"  if name in {list_of_user_defineds}:")
    body.append("    print(f'fui chamado {name}')")
    body.append("  return object.__getattribute__(self, name)")
    fn = __create_fn("__getattribute__", body)
    setattr(cls, "__getattribute__", fn)

def __process_class(cls=None):
    __set_new_attribute(cls)
    return cls

def trace(cls=None):
    def wrap(cls):
        return __process_class(cls)

    return wrap(cls)