import importlib
import inspect
import pkgutil
import sys
from typing import List

def get_classes_in_package(package_name: str) -> List[type]:
    classes = []

    package = importlib.import_module(package_name)
    package_path = getattr(package, '__path__', None)

    if package_path is None:
        # Not a package
        return classes

    for importer, modname, ispkg in pkgutil.walk_packages(package_path):
        module = importer.find_module(modname).load_module(modname)

        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and obj.__module__ == module.__name__:
                # Ensure it's a class defined in the module, not imported
                classes.append(obj)

    return classes

# Example usage:
package_name = 'your_package_name'
all_classes = get_classes_in_package(package_name)

# Now, `all_classes` contains a list of all classes defined in your package.
# You can filter out classes from third-party libraries if needed.
