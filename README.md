# Customer Tracking System Project
<img width="359" height="635" alt="Python Database Application" src="https://github.com/user-attachments/assets/09576395-1d6f-402a-9e6c-dc069b38409b" />

### Main Task 👇
Create a customer tracking system for an imaginary fiber internet company, Data Plus Fiber. The application should be able to directly interact with a created / provided database to view and / or modify the customer and product data contained with it.
________________________________________________________________________________________________________________________________________
### How I approached the task 👇
For this task, I chose to build the application in Python and embed SQL directly into the application to interact with the database. This is done by importing the SQLite3 library into my application files and creating queries to interact
directly with the database. Due to this design choice, I decided to let SQLite do most of the heavy lifting in regards to the application's functionality.
________________________________________________________________________________________________________________________________________
### Application Structure 👇
During my time creating the application, I closely followed both the modular programming techinque. Because of this, the application is split into multiple files which separates the code by which of the different types of functionality a given piece of code belongs to.

#### Files:

main.py - Main file of the application that contains all code and functions that relate to the user interface and directing the application to which option a user selects.

prompts.py - File that contains all functions that gather input from the user. These prompts include gather customer / product data, modifying existing data, and viewing existing data.

queries.py - File that houses all SQLite queries that interact with the database file.

database.py - File that acts as the middleman of sorts between the Python and SQLite parts of the application. This file contains functions that are called by the main file and then interact with the SQLite queries.

other_functions.py - File that contains functions that don't belong to any of the other four files. At the time of posting this application, this file contains functions for hard enforcing date and phone number format constraints.
________________________________________________________________________________________________________________________________________
### Application Design Process 👇
The design process I chose to follow was the agile design methodology. I acted as if this application was to be delivered to a client. Because of this I decided to break the design process into multiple steps.

#### Step 1: Gather user requirements and design database schema and application structure accordingly
Upon speaking to the client about what they desire from the customer tracking system, I determined the application needs to be able to
1. Add and remove customer data, product data, and product assignments to customers
2. Modify key elements of data already entered into the database (such as a customer's last made payments and a product's price)
3. View all of the three main elements of the database and certain subsets of them (such as customers who are late on payments and what products a specified customer has assigned to them currently)
4. A customer, product, and location can each have multiple of the same entries within the database. HOWEVER, A customer can only have one entry per location, a product can only have one entry per price point, and a customer can
   only currently be assigned a specified product one time per location. It should be noted that a customer's sign up date and last payment date can vary among multiple locations assigned to the same customer.
6. Removing or modifying an entry for one element of the database should also have its changes reflected in the other elements as well (Such as a customer being removed from the database should also remove any product assignments
   to said customer).
   
I was able to clearly define the desired user operations of the application into the following 13 options:
1. Add a customer
2. Remove a customer
3. View customer(s)
4. View customers who currently have late payments
5. Update a customer's last payment made
6. Add a product
7. Remove a product
8. View product(s)
9. Edit the price of a product
10. Assign a product to a customer
11. Unassign a product from a customer
12. View product assignment(s)
13. View a customer's monthly bill

#### Step 2. Create database schema and functionality to add and remove customer and product data.
Now that I had all user requirements defined, I decided the first step was to create the proper database schema and to create the functionality to add and remove data from the database. 

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
    
Regarding to adding and removing data functionality, we first needed to create the application structure. I described the file structure and modular design implemenation above, so no need to rehash it here. After the structure was put
into place, the functions and SQLite queries were added to the application to allowing data creation and deletion.

Once the functionality was put into place, I met with the client and ensured that all facets of the database and the data creation / deletion functionality were to their liking and I was met with a 👍.

#### Step 3. Create functionality to view and modify customer and product data
Next was on to adding the rest of the functionality related to the "customers" and "products" table. This includes viewing entries in either tables, updating the date that a customer entry made their last payment, and updating a product's price. The functionality and SQLite queries were put into the application and quality tested to ensure features were responsive and potential errors were handled.

Once the functionality was put into place, I met with the client and ensured that all desired functionality related to specfically customer and product data were implemented and up to their standards and I was met with a 👍.

#### Step 4. Create functionality to add, remove, view, and modify customer product assignment data and also view a specified customer's monthly bill
The last step in the design process was to create all functionality related to the "customer_products" table and to deliver the finished product. The implementation of the "customer_products" table went smoothly as by factoring the table
into the database schema design from the start allowed me to easily create the neccessary functionality to interact between the tables with minimal difficulty. The functionality related to the "customer_products" table was easy to design
as it is overall very similar to the two other tables. The only difficulty came from accounting for every error that can come into place when assigning a product to a customer and designing the logic for how the application determines a
customer's monthly bill.

Once all of the functionality regarding product assignment data was put into place, I quality tested every piece of functionality in the application and made sure that all functionality was properly reflected in the database and that the
user would receive clear feedback upon any modification being made. Once the application was deemed ready to ship from my end, I met with the client once more and they decided that the product contained every piece of functionality they
needed and tested it to see if it worked with the company's databases. The customer tracking system seamlessly integrated with their databases and the product was then shipped off.
