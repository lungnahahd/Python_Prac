import sqlite3
from time import sleep

conn = sqlite3.connect("test_db", isolation_level=None)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id int AUTO_INCREMENT NOT NULL PRIMARY KEY,\
    name VARCHAR(32) NOT NULL, position VARCHAR(12) NOT NULL)")

cursor.execute("INSERT INTO test_table(id, name, position) VALUES(1,'최원준','우익수')")
cursor.execute("INSERT INTO test_table(id, name, position) VALUES(2, '김선빈','2루수')")
cursor.execute("INSERT INTO test_table(id, name, position) VALUES(3, '터커','1루수')")
# cursor.execute("INSERT INTO test_table(name, position) VALUES('최형우','지명타자')")
# cursor.execute("INSERT INTO test_table(name, position) VALUES('나지완','좌익수')")
# cursor.execute("INSERT INTO test_table(name, position) VALUES('이창진','중견수')")
# cursor.execute("INSERT INTO test_table(name, position) VALUES('류지혁','3루수')")
# cursor.execute("INSERT INTO test_table(name, position) VALUES('김민식','포수')")
#  cursor.execute("INSERT INTO test_table(name, position) VALUES('박찬호','유격수')")

for i in range(1,10):
    
    cursor.execute(f'SELECT *FROM test_table WHERE id={i}')
    lineup = cursor.fetchone()
    print(f'{i}번 타자 {lineup}')



conn.commit()
conn.close()