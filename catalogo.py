
from init_mokc import monitor


class CatalogConnector:


    @monitor()
    def get_table_to_df(self, database, table, additional_param):
        print("hello from get")
   

    @monitor()
    def put_df_to_table(self, df, database, table):
        print("putt helo forom")

