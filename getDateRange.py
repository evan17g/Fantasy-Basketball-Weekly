import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("SELECT * FROM Weeks WHERE end_date < '2025-11-10' and start_date > '2025-10-26';")
weeks = cur.fetchall()

for week in weeks:
    print(week)

cur.close()