import sqlite3
import json

# Connect to in-memory DB (or file)
con = sqlite3.connect(":memory:")
cur = con.cursor()

# Create schema
cur.execute("CREATE TABLE users (id INTEGER, name TEXT, role TEXT)")
cur.execute("CREATE TABLE logs (user_id INTEGER, action TEXT)")

# Seed data
cur.executemany("INSERT INTO users VALUES (?, ?, ?)", [
    (1, "Alice", "admin"), (2, "Bob", "user"), (3, "Charlie", "user")
])
cur.executemany("INSERT INTO logs VALUES (?, ?)", [
    (1, "login"), (1, "delete_user"), (2, "login"), (3, "view_page")
])

# Complex query: Find actions by admins
res = cur.execute("""
    SELECT u.name, l.action 
    FROM users u 
    JOIN logs l ON u.id = l.user_id 
    WHERE u.role = 'admin'
""")

data = [{"name": row[0], "action": row[1]} for row in res.fetchall()]

with open("/output/analysis.json", "w") as f:
    json.dump(data, f, indent=2)
