import sqlite3

conn = sqlite3.connect('final_project.db')
cur = conn.cursor()
cur.execute('SELECT * FROM directors WHERE id = 4762')
datas = cur.fetchall()
for data in datas:
    print(data)