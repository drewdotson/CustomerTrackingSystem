# Customer Tracking System Project

I created a customer tracking system for an imaginary fiber internet company, Data Plus Fiber. The application should be able to directly interact with a created / provided database to view and / or modify the customer and product data contained with it.
<p align="center">
<img width="922" height="614" alt="Python SQLite" src="https://github.com/user-attachments/assets/acd47f38-4a16-4fb9-8876-be95c1155d63" />
</p>

________________________________________________________________________________________________________________________________________________________
### How I approached the task 👇
I built the application in Python by embedding SQLite directly into Python using the SQLite3 library to handle database interactions. This design lets SQLite manage most of the application’s core functionality.

________________________________________________________________________________________________________________________________________
### Application Structure 👇
I followed modular programming principles, organizing the application into multiple files based on functionality.

#### Files:

main.py - Main file of the application that contains all code and functions that relate to the user interface and directing the application to which option a user selects.

prompts.py - File that contains all functions that gather input from the user. These prompts include gather customer / product data, modifying existing data, and viewing existing data.

queries.py - File that houses all SQLite queries that interact with the database file.

database.py - File that acts as the middleman of sorts between the Python and SQLite parts of the application. This file contains functions that are called by the main file and then interact with the SQLite queries.

other_functions.py - File that contains functions that don't belong to any of the other four files. At the time of posting this application, this file contains functions for hard enforcing date and phone number format constraints.
________________________________________________________________________________________________________________________________________
### Application Design Process 👇
I followed an agile design methodology, treating this project as if it were being delivered to a client. The process was divided into clear, iterative steps.

#### Step 1. Define user requirements and design the database schema
After gathering requirements from the client, I determined the system needed to:
   1. Add, remove, and modify customer and product data
   2. Assign and unassign products to customers
   3. View customers, products, and their relationships (e.g., late payments, active product assignments)
   4. Maintain data integrity — e.g., removing a customer automatically removes their product assignments

From these needs, I defined 13 key user operations, including adding/removing customers or products, updating data, and viewing customer bills.

#### Step 2. Build the database schema and CRUD functionality
With requirements defined, I created the initial SQLite database schema and implemented add/remove (CRUD) operations.
The schema consists of three main tables:

Regarding the database schema, I decided that three tables needed to be created (one for customer data, one for product data, and one for product assignments for customers present in the database). Factoring into the constraints, the
"customers" table needed to be forced to have unique customer name and location combinations for each entry. The "products" table needed to be forced to have unique product name and price combinations for each entry. Finally, the
"customer_products" table needed to take customer name + location combinations and product name + price combinations as its own unique combinations for each entry. This schema allowed for the desired flexibility while also preventing
duplicate entries and possible orphan entries if one of the foreign keys happened to be deleted from its original table.

DATABASE SCHEMA 👇

##### customers
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone_num VARCHAR(12),
    location TEXT,
    card_num TEXT,
    sign_up_date REAL,
    last_payment REAL,
    UNIQUE(name, location)
##### products
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    product_type TEXT,
    price FLOAT,
    UNIQUE(product, price)
##### customer_products
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    customer_location TEXT,
    product_name TEXT,
    product_price FLOAT,
    unique(customer_name, customer_location, product_name, product_price),
    FOREIGN KEY (customer_name, customer_location) REFERENCES customers(name, location) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (product_name, product_price) REFERENCES products(product, price) ON DELETE CASCADE ON UPDATE CASCADE)
    
This schema prevents duplicate or orphaned entries and maintains referential integrity between tables.
After implementing the CRUD operations, I reviewed the functionality with the client — all requirements were met. ✅

#### Step 3. Add functionality to view and update customer and product data
Next, I implemented features for:

   * Viewing customer and product entries
   * Updating a customer’s last payment date
   * Editing product prices

These operations were built using modularized SQLite queries. After testing for responsiveness and error handling, the client confirmed all functions worked as intended. ✅.

#### Step 4. Implement customer-product assignment and billing features
Finally, I created all logic related to the customer_products table, including:

   * Assigning/unassigning products to customers
   * Viewing current assignments
   * Generating a customer’s monthly bill

Because this functionality was considered early in the schema design, integration was smooth. The main challenge was handling edge cases in product assignments and ensuring data remained consistent across all tables.

After full testing and validation with the client, the system was successfully integrated with their existing databases and delivered as the final product. 🚀
