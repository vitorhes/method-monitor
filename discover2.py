from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Define the number of columns
num_columns = 200

# Create a DataFrame with 200 columns filled with null values
df = spark.range(1).select([col(f"Column_{i}").cast("string").alias(f"Column_{i}") for i in range(num_columns)])

# Add rows to the DataFrame
new_rows = [(f"value_{j}" for j in range(num_columns)) for i in range(5)]  # Assuming 5 rows
new_df = spark.createDataFrame(new_rows, [f"Column_{i}" for i in range(num_columns)])

# Union the DataFrames to combine the original and new rows
result_df = df.union(new_df)

# Show the resulting DataFrame
result_df.show(truncate=False)
