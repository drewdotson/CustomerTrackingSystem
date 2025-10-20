
# NOTE: This file contains all functions that interact directly with the SQLite queries. Consider this file as the
# "bridge" between the python and the SQL.

import sqlite3
from datetime import datetime, timedelta
import queries

#-----------------------------------------------------------------------------------------------------------------#

connection = sqlite3.connect("customer_data.db")
connection.execute("PRAGMA foreign_keys = ON")

# MAIN FUNCTIONS 👇 ---------------------------------------------------------------------------------------------#

# Function used to create tables if they do not already exist
def create_tables():
    with connection:
        connection.execute(queries.CREATE_CUSTOMERS_TABLE)
        connection.execute(queries.CREATE_PRODUCTS_TABLE)
        connection.execute(queries.CREATE_CUSTOMER_PRODUCTS_TABLE)


# Function used for 👇
# 1. Add a customer
def add_new_customer(name, phone_num, location, card_num, sign_up_timestamp, last_payment_timestamp):
    with connection:
        connection.execute(queries.INSERT_CUSTOMER, (name, phone_num, location, card_num, sign_up_timestamp, last_payment_timestamp))


# Functions used for 👇
# 2. Remove a customer
def remove_customer(id, customer_name):
    with connection:
        connection.execute(queries.REMOVE_CUSTOMER, (id, customer_name))
def view_customer_info(name):
    cursor = connection.cursor()
    cursor.execute(queries.VIEW_CUSTOMER_INFO, (name, ))
    return cursor
    

# Function used for 👇
# 3. View customer(s)
def view_customers():
    cursor = connection.cursor()
    cursor.execute(queries.VIEW_ALL_CUSTOMERS)
    return cursor


# Function used for 👇
# 4. View customers who currently have late payments
def view_late_customers():
    late_payment_threshold = (datetime.now() - timedelta(days=30)).timestamp()
    cursor = connection.cursor()
    cursor.execute(queries.VIEW_LATE_CUSTOMERS, (late_payment_threshold, ))
    return cursor


# Function used for 👇
# 5. Update a customer's last payment made
def update_last_payment(last_payment_timestamp, entry_to_update):
    with connection:
        connection.execute(queries.UPDATE_LAST_PAYMENT, (last_payment_timestamp, entry_to_update))
# NOTE: view_customer_info() is also used for option # 5.


# Function used for 👇
# 6. Add a product
def add_new_product(product, type, price):
    with connection:
        connection.execute(queries.INSERT_PRODUCT, (product, type, price))


# Functions used for 👇
# 7. Remove a product
def remove_product(id, product):
    with connection:
        connection.execute(queries.REMOVE_PRODUCT, (id, product))
def view_product_info(product):
    cursor = connection.cursor()
    cursor.execute(queries.VIEW_PRODUCT_INFO, (product, ))
    return cursor


# Function used for 👇
# 8. View product(s)
def view_products():
    cursor = connection.cursor()
    cursor.execute(queries.VIEW_ALL_PRODUCTS)
    return cursor


# Function used for 👇
# 9. Edit the price of a product
def update_price(price, entry_to_update):
    with connection:
        connection.execute(queries.UPDATE_PRICE, (price, entry_to_update))
# NOTE: view_product_info() is also used for option # 5.


# Function used for 👇
# 10. View a customer's monthly bill
def assign_product_to_customer(customer_name, customer_location, product_to_assign, price_to_assign):
    with connection:
        connection.execute(queries.ASSIGN_PRODUCT_TO_CUSTOMER, (customer_name, customer_location, product_to_assign, price_to_assign))


# Function used for 👇
# 11. Remove a product from a customer
def remove_assignment(id):
    with connection:
        connection.execute(queries.REMOVE_ASSIGNMENT, (id, ))


# Function used for 👇
# 12. View product assignment(s)
def view_assignments():
    cursor = connection.cursor()
    cursor.execute(queries.VIEW_ALL_ASSIGNMENTS)
    return cursor


# Function used for 👇
# 13. View a customer's monthly bill
def view_monthly_bill(name):
    cursor = connection.cursor()
    cursor.execute(queries.CUSTOMER_TOTAL_BILL, (name, ))
    return cursor

# CHECK FUNCTIONS 👇 --------------------------------------------------------------------------------------------#

# Function used to check if a specified customer and location combination exists in the database
def customer_at_location_check(name, location):
    cursor = connection.cursor()
    cursor.execute(queries.CHECK_CUSTOMER_EXISTS_AT_LOCATION, (name, location))
    if len(cursor.fetchall()) == 0:
        return False
    else:
        return True


# Function used to check if a specified product and price combination exists in the database.
def product_and_price_check(product, price):
    cursor = connection.cursor()
    cursor.execute(queries.CHECK_PRODUCT_AND_PRICE_EXISTS, (product, price))
    if len(cursor.fetchall()) == 0:
        return False
    else:
        return True


# Function used to check if a specified customer ID exists in the customers table
def id_check_customers(id, name):
    cursor = connection.cursor()
    cursor.execute(queries.CHECK_CUSTOMER_ID, (id, name))
    if len(cursor.fetchall()) == 0:
        return False
    else:
        return True


# Function used to check if a specified product ID exists in the products table
def id_check_products(id, product):
    cursor = connection.cursor()
    cursor.execute(queries.CHECK_PRODUCT_ID, (id, product))
    if len(cursor.fetchall()) == 0:
        return False
    else:
        return True
    

# Function used to check if a specified product assignment ID exists in the customer_products table
def id_check_customer_products(id):
    cursor = connection.cursor()
    cursor.execute(queries.CHECK_ASSIGNMENT_ID, (id, ))
    if len(cursor.fetchall()) == 0:
        return False
    else:
        return True
    

# Function used to check if a specified customer name exists in the customers table
def customer_check(name):
    cursor = connection.cursor()
    cursor.execute(queries.CHECK_CUSTOMER_EXISTS, (name, ))
    if len(cursor.fetchall()) == 0:
        return False
    else:
        return True


# Function used to check if a specified product name exists in the products table
def product_check(product):
    cursor = connection.cursor()
    cursor.execute(queries.CHECK_PRODUCT_EXISTS, (product, ))
    if len(cursor.fetchall()) == 0:
        return False
    else:
        return True


# Function used to check if a customer has any product assigned to them
def customer_assignment_check(name):
    cursor = connection.cursor()
    cursor.execute(queries.CHECK_CUSTOMER_ASSIGNMENT_EXISTS, (name, ))
    if len(cursor.fetchall()) == 0:
        return False
    else:
        return True
