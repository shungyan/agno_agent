import sqlite3

conn = sqlite3.connect("./agent/agno.db")
cursor = conn.cursor()

cursor.execute("SELECT session_id FROM agno_sessions;")
session_id = cursor.fetchall()
print(session_id)

conn.close()