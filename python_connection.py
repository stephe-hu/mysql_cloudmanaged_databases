import os
from dotenv import load_dotenv
from pandas import read_sql, DataFrame
from sqlalchemy import create_engine, inspect

from populate import insert_fake_data

# Load environment variables from .env file
load_dotenv() 

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)


def get_tables(engine):
    """Get list of tables."""
    inspector = inspect(engine)
    return inspector.get_table_names()

def execute_query_to_dataframe(query: str, engine):
    """Execute SQL query and return result as a DataFrame."""
    return read_sql(query, engine)


# Example usage
tables = get_tables(db_engine)
print("Tables in the database:", tables)

# Call the insert_fake_data function to populate the database with fake data
insert_fake_data(db_engine)

# Retrieve data from the 'providers' table
sql_query_providers = "SELECT * FROM patients"  # Modify as per your table
providers_df = execute_query_to_dataframe(sql_query_providers, db_engine)

# Print the DataFrame
print("Data from 'providers' table:")
print(providers_df)
