import sqlite3
from tqdm import tqdm
import fireducks.pandas as pandas

# Connect to SQLite database
db_path = "database/db.sqlite3"
conn = sqlite3.connect(db_path)

# Get all table names
tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = [row[0] for row in conn.execute(tables_query).fetchall()]

# Export each table as a CSV file
for table in tqdm(tables):
    df = pandas.read_sql_query(f"SELECT * FROM {table};", conn)
    df.to_csv(f"database/table_records/{table}.csv", index=False)
    print(f"Exported {table}.csv")

# Close connection
conn.close()
