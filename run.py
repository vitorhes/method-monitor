from catalogo import CatalogConnector
# Example usage:
conn = CatalogConnector()

#conn.get_table_to_df(database="db", table="tabela1", additional_param="extra_info")
conn.get_table_to_df("db","table",additional_param="as")

# This will print the simulated HTTP request with the payload

#conn.put_df_to_table("db","tabela1","extra_info")
#conn.put_df_to_table(df="df2",database="db", table="tabela1")