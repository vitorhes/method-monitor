import inspect
from functools import wraps

def capture_arguments(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Get the function signature
        signature = inspect.signature(func)
        
        # Bind the arguments to the parameters
        bound_arguments = signature.bind(*args, **kwargs)
        bound_arguments.apply_defaults()

        # Print parameter names and values
        print(f"Function {func.__name__} called with arguments:")
        for param_name, param_value in bound_arguments.arguments.items():
            print(f"{param_name}: {param_value}")

        return func(*args, **kwargs)

    return wrapper

# Example usage:
@capture_arguments
def example_function(a, b, c=10):
    pass

example_function(1, b=2, c=20)
