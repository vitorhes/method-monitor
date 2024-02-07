from typing import List, Optional, Callable, Union, Dict
from payload_handler import PayloadHandler
import threading
import uuid


class MonitorFactory:
    def __init__(self) -> None:
        self.generated_uuid = str(uuid.uuid4())

    def __call__(self, *params_to_collect: Union[str, None]) -> Callable:
        """
        Decorator factory. If params_to_collect is empty, collect all parameters. 
        If specified, collect only the specified parameters.

        Args:
            *params_to_collect (Union[str, None]): Parameters to collect if specified.

        Returns:
            Callable: Decorator function.
        """
        def decorator(method: Callable) -> Callable:
            """
            Decorator function.

            Args:
                method (Callable): Original method.

            Returns:
                Callable: Decorated method.
            """
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
                    if params_to_collect:
                        # Collect only specified parameters
                        arguments = {param: kwargs.get(param) if param in kwargs else args[i] for i, param in enumerate(params_to_collect)}
                    else:
                        # Collect all parameters
                        arguments = {f"arg_{i}": arg for i, arg in enumerate(args)}
                        arguments.update(kwargs)
                    
                    submodule_name = method.__module__
                    payload = {"method": method.__name__, "arguments": arguments}
                    
                    thread = threading.Thread(target=PayloadHandler.create_and_send, args=(submodule_name, payload, self.generated_uuid,), daemon=True)
                    thread.start()
                    
                    return method(instance, *args, **kwargs)
                except Exception as e:
                    return method(instance, *args, **kwargs)
                    pass

            return wrapper

        return decorator
