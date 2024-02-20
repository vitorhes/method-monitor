import importlib
import pkgutil

def get_all_classes(module):
    classes = []
    for obj_name in dir(module):
        obj = getattr(module, obj_name)
        if isinstance(obj, type):
            classes.append(obj)
        elif inspect.ismodule(obj):
            # Recursively get classes from nested modules
            classes.extend(get_all_classes(obj))
    return classes

__all__ = [module_name for _, module_name, _ in pkgutil.iter_modules(globals()['__path__'])]

# Import all classes from discovered modules
classes_to_patch = []
for module_name in __all__:
    module = importlib.import_module(f"{__package__}.{module_name}")
    classes_to_patch.extend(get_all_classes(module))
