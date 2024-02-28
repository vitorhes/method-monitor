def import_class(module_name, class_name):
    module = __import__(module_name, fromlist=[class_name])
    return getattr(module, class_name)

# Example list of classes
class_list = [someouther.Another, somemodule.Etc, somemodulei.Testei]

# Package name
package_name = "datautils"

# Iterate over the classes and import them with full names
imported_classes = []
for dynamic_class in class_list:
    module_name = dynamic_class.__module__

    # Check if the module name starts with the package name
    if not module_name.startswith(package_name):
        module_name = f"{package_name}.{module_name}"

    local_class_name = dynamic_class.__name__
    full_class_name = f"{module_name}.{local_class_name}"
    imported_class = import_class(module_name, local_class_name)
    imported_classes.append(imported_class)

# Now, 'imported_classes' contains the dynamically imported classes with their full names
for dynamic_class in imported_classes:
    print(dynamic_class)
