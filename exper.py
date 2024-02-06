class MethodMonitor:
    def __call__(self, *params_to_collect):
        def decorator(method):
            def wrapper(instance, *args, **kwargs):
                arguments = {param: value for param, value in zip(params_to_collect, args)}
                arguments.update(kwargs)
                
                payload = {"method": method.__name__, "arguments": arguments}
                self.send_http_request(payload)
                return method(instance, *args, **kwargs)

            return wrapper

        return decorator

    def send_http_request(self, payload):
        print(f"Sending HTTP request with payload: {payload}")


class CatalogConnector:
    metadata_updater = MethodMonitor()

    @metadata_updater("database", "table")
    def get_table_to_df(self, database, table, additional_param):
        print("hello")
   

    @metadata_updater("df", "database", "table")
    def put_df_to_table(self, df, database, table):
        print("putt")

