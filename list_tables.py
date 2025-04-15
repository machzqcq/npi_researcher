import duckdb

# Connect to the DuckDB database
db_path = 'data_etl/medicare_data.duckdb'
con = duckdb.connect(db_path)

# Define a query to find prescribers associated with 'University of Washington Medical Center'
query = """
SELECT *
FROM medicare_data
WHERE LOWER(Prscrbr_Last_Org_Name) LIKE '%university of washington medical center%'
   OR LOWER(Prscrbr_Last_Org_Name) LIKE '%uw medical center%'
   OR LOWER(Prscrbr_Last_Org_Name) LIKE '%university of washington%'
   OR LOWER(Prscrbr_Practice_Location_Address_City_Name) LIKE '%seattle%'
   OR LOWER(Prscrbr_Practice_Location_Address_State_Name) = 'wa'
LIMIT 100;
"""

# Execute the query and fetch results
try:
    result = con.execute(query).fetchdf()
    print("Query executed successfully. Results:")
    print(result)
except Exception as e:
    print(f"An error occurred while executing the query: {e}")
finally:
    con.close()