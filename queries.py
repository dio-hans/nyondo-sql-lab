import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM products;")

# fetch results
rows = cursor.fetchall()

# print results
for row in rows:
    print(row)

conn.close()