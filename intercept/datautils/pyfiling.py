def track_method_call(func):
    def wrapper(*args, **kwargs):
        method_name = func.__name__
        # Send information to the desired HTTP endpoint
        print("MONKEY PATCHING")
        payload = {'method': method_name, 'arguments': {'args': args, 'kwargs': kwargs}}
        ProfilingFactory.instance().add_payload(payload)

        # Call the original method
        return func(*args, **kwargs)

    return wrapper

class ProfilingFactory:
    _instance = None
    _payload_list = []

    def __init__(self, classes: list) -> None:
        self.classes = classes
        for classe in classes:
            self.__monkey_patch(classe)

    def __monkey_patch(self, classe: object):
        for attr_name, attr_value in vars(classe).items():
            if callable(attr_value):
                setattr(classe, attr_name, track_method_call(attr_value))
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def add_payload(cls, payload):
        cls.instance()._payload_list.append(payload)

    @classmethod
    def get_payload_list(cls):
        return cls.instance()._payload_list.copy()
