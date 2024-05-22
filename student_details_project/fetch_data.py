import sqlite3

conn = sqlite3.connect('students.db')
c = conn.cursor()
c.execute('SELECT * FROM students')
rows = c.fetchall()
conn.close()

for row in rows:
    print(row)

