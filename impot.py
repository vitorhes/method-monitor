from thread import CatalogConnector


# Example usage:
conn = CatalogConnector()

conn.get_table_to_df(database="db", table="tabela1", additional_param="extra_info")
# This will print the simulated HTTP request with the payload

conn.put_df_to_table("db","tabela1","extra_info")
