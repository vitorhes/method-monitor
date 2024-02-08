# __init__.py in the datautils package

import pkgutil
import importlib
from .main import MyClass

from .pyfiling import ProfilingFactory
# Discover and import all modules in the current package
__all__ = [
    module_name for _, module_name, _ in pkgutil.iter_modules(__path__)
]

# Import all classes from discovered modules
classes_to_patch = []
for module_name in __all__:
    module = importlib.import_module(f"{__name__}.{module_name}")
    for obj_name in dir(module):
        obj = getattr(module, obj_name)
        if isinstance(obj, type):
            classes_to_patch.append(obj)

# Apply monkey patching using ProfilingFactory
profiling_factory = ProfilingFactory(classes_to_patch)

payload_list = profiling_factory.instance().get_payload_list()
print(f"Singleton Payload List: {payload_list}")