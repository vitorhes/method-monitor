import threading

class MethodMonitor:
    def __call__(self, *params_to_collect):
        def decorator(method):
            def wrapper(instance, *args, **kwargs):
                try:
                    arguments = {param: value for param, value in zip(params_to_collect, args)}
                    arguments.update(kwargs)
                    
                    payload = {"method": method.__name__, "arguments": arguments}
                    thread = threading.Thread(target=PayloadSender.send_http_request, args=(payload,))
                    thread.start()
                    return method(instance, *args, **kwargs)
                except Exception as e:
                    return method(instance, *args, **kwargs)

            return wrapper

        return decorator


class PayloadSender:
    @staticmethod
    def send_http_request(payload):
        current_thread = threading.current_thread()
        print(f"Sending HTTP request with payload: {payload} from thread {current_thread.name} ({current_thread.ident})")

class CatalogConnector:
    metadata_updater = MethodMonitor()

    @metadata_updater("database", "table")
    def get_table_to_df(self, database, table, additional_param):
        print("hello")
   
    @metadata_updater("df", "database", "table")
    def put_df_to_table(self, df, database, table):
        print("putt")

