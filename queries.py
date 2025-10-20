 
# NOTE: This file contains all the SQLite queries that are needed for every present functionality in the application.

# CREATE STATEMENTS 👇 ------------------------------------------------------------------------------------------#

CREATE_CUSTOMERS_TABLE = """CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone_num VARCHAR(12),
    location TEXT,
    card_num TEXT,
    sign_up_date REAL,
    last_payment REAL,
    UNIQUE(name, location));"""


CREATE_PRODUCTS_TABLE = """CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    product_type TEXT,
    price FLOAT,
    UNIQUE(product, price));"""


CREATE_CUSTOMER_PRODUCTS_TABLE = """CREATE TABLE IF NOT EXISTS customer_products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    customer_location TEXT,
    product_name TEXT,
    product_price FLOAT,
    unique(customer_name, customer_location, product_name, product_price),
    FOREIGN KEY (customer_name, customer_location) REFERENCES customers(name, location) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (product_name, product_price) REFERENCES products(product, price) ON DELETE CASCADE ON UPDATE CASCADE);"""

# INSERT STATEMENTS 👇 ----------------------------------------------------------------------------------------#

INSERT_CUSTOMER = """INSERT INTO customers(name, phone_num, location, card_num, sign_up_date, last_payment)
    VALUES (?, ?, ?, ?, ?, ?);"""


INSERT_PRODUCT = "INSERT INTO products(product, product_type, price) VALUES (?, ?, ?);"


ASSIGN_PRODUCT_TO_CUSTOMER = "INSERT INTO customer_products(customer_name, customer_location, product_name, product_price) VALUES (?, ?, ?, ?);"

# VIEW STATEMENTS 👇 ----------------------------------------------------------------------------------------#

VIEW_ALL_CUSTOMERS = "SELECT id, name, phone_num, location, card_num, sign_up_date, last_payment FROM customers;"


VIEW_ALL_PRODUCTS = "SELECT id, product, product_type, price FROM products;"


VIEW_ALL_ASSIGNMENTS = "SELECT id, customer_name, customer_location, product_name, product_price FROM customer_products;"


VIEW_CUSTOMER_INFO = "SELECT id, name, phone_num, location, card_num, sign_up_date, last_payment FROM customers WHERE name = ?;"


VIEW_PRODUCT_INFO = "SELECT id, product, product_type, price FROM products WHERE product = ?;"


VIEW_LATE_CUSTOMERS = "SELECT id, name, phone_num, location, card_num, sign_up_date, last_payment FROM customers WHERE last_payment < ?;"


VIEW_CUSTOMER_NAME_LOCATION = "SELECT name, location FROM customers WHERE id = ?;"

# DELETE STATEMENTS 👇 ----------------------------------------------------------------------------------------#

REMOVE_CUSTOMER = "DELETE FROM customers WHERE id = ? and name = ?;"


REMOVE_PRODUCT = "DELETE FROM products WHERE id = ? and product = ?;"


REMOVE_ASSIGNMENT = "DELETE FROM customer_products WHERE id = ?"

# UPDATE STATEMENTS 👇 ----------------------------------------------------------------------------------------#

UPDATE_LAST_PAYMENT = "UPDATE customers SET last_payment = ? WHERE id = ?;"


UPDATE_PRICE = "UPDATE products SET price = ? WHERE id = ?;"

# CHECK STATEMENTS 👇 -----------------------------------------------------------------------------------------#

CHECK_CUSTOMER_EXISTS_AT_LOCATION = "SELECT * FROM customers WHERE name = ? AND location = ?;"


CHECK_PRODUCT_AND_PRICE_EXISTS = "SELECT * FROM products WHERE product = ? AND price = ?;"


CHECK_CUSTOMER_ASSIGNMENT_EXISTS = "SELECT * FROM customer_products WHERE customer_name = ?;"


CHECK_CUSTOMER_ID = "SELECT * FROM customers WHERE id = ? AND name = ?;"


CHECK_PRODUCT_ID = "SELECT * FROM products WHERE id = ? and product = ?;"


CHECK_ASSIGNMENT_ID = "SELECT * FROM customer_products WHERE id = ?;"


CHECK_CUSTOMER_EXISTS = "SELECT * FROM customers WHERE name = ?;"


CHECK_PRODUCT_EXISTS = "SELECT * FROM products WHERE product = ?;"

# SUM STATEMENT 👇 -----------------------------------------------------------------------------------------#

CUSTOMER_TOTAL_BILL = "SELECT printf(\"%.2f\", SUM(product_price)) FROM customer_products WHERE customer_name = ?;"
