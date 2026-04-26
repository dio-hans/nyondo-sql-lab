import sqlite3
conn = sqlite3.connect('nyondo_stock.db')

# TODO: rewrite using ? placeholder - never use f-strings in SQL
def search_product_safe(name):
    query = "SELECT * FROM products WHERE name LIKE ?"
    param = f"%{name}%"
    
    print("Query:", query)
    print("Params:", param)
    
    rows = conn.execute(
        query, (param,)).fetchall()  # ✅ correct
    print(f'Result: {rows}\n')
    return rows

def login_safe(username, password):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    
    print("Query:", query)
    print("Params:", (username, password))
    
    row = conn.execute(query, (username, password)).fetchone()
    print(f"Result: {row}\n")
    
    return row

# These must ALL return [] or None when you run them
print('Test 1:', search_product_safe("' OR 1=1--"))
print('Test 2:', search_product_safe("' UNION SELECT id,username,password,role FROM users--"))
print('Test 3:', login_safe("admin'--", 'anything'))
print('Test 4:', login_safe("' OR '1'='1", "' OR '1'='1"))