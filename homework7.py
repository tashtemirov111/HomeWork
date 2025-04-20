import sqlite3

def create_connection(hw_db):
    conn = None
    try:
        conn = sqlite3.connect(hw_db)
        print("Connection created successfully")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(connection):
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL CHECK(LENGTH(product_title) <= 200),
        price REAL NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        print("Table created successfully")
    except sqlite3.Error as e:
        print(e)

def insert_products(connection):
    products = [
        ("Мыло детское", 45.5, 10),
        ("Жидкое мыло с запахом ванили", 75.0, 15),
        ("Шампунь", 120.0, 20),
        ("Зубная паста", 60.0, 8),
        ("Зубная щетка", 35.0, 30),
        ("Гель для душа", 95.0, 12),
        ("Салфетки влажные", 25.0, 50),
        ("Туалетная бумага", 20.0, 100),
        ("Стиральный порошок", 300.0, 5),
        ("Освежитель воздуха", 150.0, 6),
        ("Пена для бритья", 110.0, 7),
        ("Бритва", 200.0, 4),
        ("Дезодорант", 130.0, 10),
        ("Мочалка", 40.0, 25),
        ("Крем для рук", 90.0, 11)
    ]
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", products)
    connection.commit()
    print("15 products inserted successfully")

def update_quantity(connection, product_id, new_quantity):
    cursor = connection.cursor()
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    connection.commit()
    print(f"Quantity for product ID {product_id} updated to {new_quantity}")

def update_price(connection, product_id, new_price):
    cursor = connection.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    connection.commit()
    print(f"Price for product ID {product_id} updated to {new_price}")

def delete_product(connection, product_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    connection.commit()
    print(f"Product ID {product_id} deleted")

def print_all_products(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    print("All products:")
    for row in rows:
        print(row)

def print_products_under_price_and_quantity(connection, price_limit, quantity_limit):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE price < ? AND quantity > ?", (price_limit, quantity_limit))
    rows = cursor.fetchall()
    print(f"Products cheaper than {price_limit} and quantity more than {quantity_limit}:")
    for row in rows:
        print(row)

def search_products_by_title(connection, keyword):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE product_title LIKE ?", (f"%{keyword}%",))
    rows = cursor.fetchall()
    print(f"Search results for '{keyword}':")
    for row in rows:
        print(row)

if __name__ == "__main__":
    db_name = "hw.db"
    conn = create_connection(db_name)
    if conn:
        create_table(conn)
        insert_products(conn)

        print("\n-- Testing update quantity (id=1, quantity=50) --")
        update_quantity(conn, 1, 50)

        print("\n-- Testing update price (id=2, price=99.99) --")
        update_price(conn, 2, 99.99)

        print("\n-- Testing delete product (id=3) --")
        delete_product(conn, 3)

        print("\n-- Testing print all products --")
        print_all_products(conn)

        print("\n-- Testing print products under price 100 and quantity over 5 --")
        print_products_under_price_and_quantity(conn, 100, 5)

        print("\n-- Testing search by title (keyword='мыло') --")
        search_products_by_title(conn, "мыло")

        conn.close()
    else:
        print("Failed to connect to database")