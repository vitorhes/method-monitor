import inspect
from typing import Optional, Callable
from payload_handler import PayloadHandler
import threading
import uuid


class MonitorFactory:
    def __init__(self) -> None:
        self.generated_uuid = str(uuid.uuid4())

    def __call__(self, method: Callable) -> Callable:
        """
        Decorator function.

        Args:
            method (Callable): Original method.

        Returns:
            Callable: Decorated method.
        """
        parameters = inspect.signature(method).parameters

        def wrapper(instance: object, *args, **kwargs) -> Optional[object]:
            """
            Wrapper function around the original method.

            Args:
                instance (object): Instance of the class.
                *args: Positional arguments.
                **kwargs: Keyword arguments.

            Returns:
                Optional[object]: Result of the original method.
            """
            try:
                # Get parameter names from the original method
                parameter_names = list(parameters.keys())
                
                # Create a dictionary with parameter names as keys
                arguments = {param: kwargs.get(param, None) for param in parameter_names}
                
                submodule_name = method.__module__
                payload = {"method": method.__name__, "arguments": arguments}
                
                thread = threading.Thread(target=PayloadHandler.create_and_send, args=(submodule_name, payload, self.generated_uuid,), daemon=True)
                thread.start()
                
            except Exception as e:
                # Handle the exception as needed (e.g., log it)
                print(f"Exception in {method.__name__}: {e}")

            # Return the result of the original method
            return method(instance, *args, **kwargs)

        return wrapper

