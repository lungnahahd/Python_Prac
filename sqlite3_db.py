import sqlite3

conn = sqlite3.connect("test_db", isolation_level=None)
cursor = conn.cursor()
#cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INT PRMIMARY KEY AUTO_INCREMENT, \
#name VARCHAR(32) NOT NULL, position VARCHAR(12) NOT NULL)")

cursor.execute("INSERT INTO test_table(name, position) VALUES('최원준','우익수')")
cursor.execute("INSERT INTO test_table(name, position) VALUES('김선빈','2루수')")
cursor.execute("INSERT INTO test_table(name, position) VALUES('터커','1루수')")
cursor.execute("INSERT INTO test_table(name, position) VALUES('최형우','지명타자')")
cursor.execute("INSERT INTO test_table(name, position) VALUES('나지완','좌익수')")
cursor.execute("INSERT INTO test_table(name, position) VALUES('이창진','중견수')")
cursor.execute("INSERT INTO test_table(name, position) VALUES('류지혁','3루수')")
cursor.execute("INSERT INTO test_table(name, position) VALUES('김민식','포수')")
cursor.execute("INSERT INTO test_table(name, position) VALUES('박찬호','유격수')")



conn.commit()
conn.close()