import threading

class MethodMonitor:
    def __call__(self, *params_to_collect):
        def decorator(method):
            def wrapper(instance, *args, **kwargs):
                arguments = {param: value for param, value in zip(params_to_collect, args)}
                arguments.update(kwargs)
                
                payload = {"method": method.__name__, "arguments": arguments}
                thread= threading.Thread(
                    target=PayloadSender.send_http_request,
                    args=(payload,), daemon=True)
                thread.start()
                #thread.join()  # Wait for the thread to finish
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
        current_thread = threading.current_thread()
        print(f"get from thread {current_thread.name} ({current_thread.ident})")
   
    @metadata_updater("df", "database", "table")
    def put_df_to_table(self, df, database, table):
        current_thread = threading.current_thread()
        print(f"put from thread {current_thread.name} ({current_thread.ident})")

