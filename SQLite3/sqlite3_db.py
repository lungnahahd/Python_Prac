import sqlite3

conn = sqlite3.connect("test_db", isolation_level=None)
cursor = conn.cursor()
#cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INT PRMIMARY KEY AUTO_INCREMENT, \
#name VARCHAR(32) NOT NULL, position VARCHAR(12) NOT NULL)")

cursor.execute()

conn.commit()
conn.close()