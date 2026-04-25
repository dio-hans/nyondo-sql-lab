# QUERY A
import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM products;")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
print('\n')

# query B

conn = sqlite3.connect('nyondo_stock.db')

cursor = conn.cursor()

cursor.execute("SELECT name, price FROM products;")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
print('\n')

# query C

conn = sqlite3.connect('nyondo_stock.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM products WHERE id = 3;")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
print('\n')

# query D

conn = sqlite3.connect('nyondo_stock.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM products WHERE name LIKE '%sheet%';")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
print('\n')

# query E

conn = sqlite3.connect('nyondo_stock.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM products ORDER BY price DESC;")


rows = cursor.fetchall()


for row in rows:
    print(row)

conn.close()
print('\n')


# query F

conn = sqlite3.connect('nyondo_stock.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM products ORDER BY price DESC LIMIT 2;")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
print('\n')

# QUERY G

conn = sqlite3.connect('nyondo_stock.db')

cursor = conn.cursor()

cursor.execute("UPDATE products SET price = 38000 WHERE id = 1;")

conn.commit()

print(cursor.fetchone())

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
