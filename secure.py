import sqlite3
conn = sqlite3.connect('nyondo_stock.db')

# TODO: rewrite using ? placeholder - never use f-strings in SQL
def search_product_safe(product_name, price=None):

    # your code here
    query = "SELECT * FROM products WHERE name LIKE ?"
    param = f"%{product_name}%"

    if not isinstance(product_name, str) or len(product_name) < 2:
        return [] # Or return "Rejected" based on your needs
    
    if any(char in product_name for char in ["<", ">", ";"]):
        return "Rejected"
    if not isinstance(price, (int, float)) or price <= 0:
            return "Rejected: price must not be a float"
    
    print("Query:", query)
    print("Params:", param)
    
    rows = conn.execute(
        query, (param,)).fetchall()  
    print(f'Result: {rows}\n')
    return rows

def login_safe(username, password):

     # your code here
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    # 1. this rejects usernames with spaces
    if not isinstance(username, str) or username == " ":
        return("Rejected: username can not be empty")
    
    if not isinstance(password, str) or len(password) < 6:
        return "rejected: password must be atleast 6 characters"

    print("Params:", (username, password))

    row = conn.execute(query, (username, password)).fetchone()
    print("Query:", query)
    print(f"Result: {row}\n")
    
    return row

# TASK 5 TEST CACES
print("Product Search Tests")

print(f"Test 'cement': {search_product_safe('cement')}") 

print(f"Test empty string: {search_product_safe('')}") 

print(f"Test '<script>': {search_product_safe('<script>')}") 

print("\n Login Tests ")

print(f"Test valid login: {login_safe('admin', 'admin123')}") 

print(f"Test short password: {login_safe('admin', 'ab')}") 

print(f"Test space in username: {login_safe('ad min', 'pass123')}")