import sqlite3

# Path to your .db file
db_file = "agno.db"

# Connect to the database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Example: List all tables
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cursor.fetchall()
# print("Tables:", tables)

# # Example: Read data from a table (replace 'your_table_name' with actual table)
table_name = "agno_sessions"
cursor.execute(f"SELECT session_id FROM {table_name} LIMIT 100;")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close connection
conn.close()

# cursor.execute(f"PRAGMA table_info({table_name});")
# columns = cursor.fetchall()

# for col in columns:
#     print(col)

# conn.close()
