
# This application is a customer tracking system for an imaginary fiber internet company, Data Plus Fiber.
# You can edit almost any aspect of a customer's and product's relationship with the company or with each other.
# The application functions by using SQLite queries to view and modify a database, customer_data.db

# NOTE: This is the main file for the customer tracking system. This file contains the user interface and functionality
# allowing the user to interact with all avaiable options. All other functionality is delegated to the other files for
# the application.

import database
import prompts
import sqlite3


# This is the menu that is displayed to the user at application start and after performing an option.
user_menu = '''\nOptions (enter option #):
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
14. Exit

Selection: '''


# MAIN 👇 -------------------------------------------------------------------------------------------------------#

try:

    # When the application is initialized, a welcome message is displayed and the database is created if it does
    # not already exist.
    print("\nWelcome to Data Plus Fiber's customer tracking system!")
    database.create_tables()

    # The application loops until the user enters "14" or keyboard interrupts to exit the customer tracking system.
    while (user_input := input(user_menu)) != "14":


        # Option 1. Add a customer
        if user_input == "1":

            # The user inputs from the prompt act as the fields that will be inserted into the customers table.
            name, phone_num, location, card_num, sign_up_timestamp, last_payment_timestamp = prompts.prompt_add_customer()
            
            # If the customer name and location combination does not already exist in the customers table, the customer
            # entry is added to the customers table and the application displays a confirmation message.
            if not database.customer_at_location_check(name, location):
                database.add_new_customer(name, phone_num, location, card_num, sign_up_timestamp, last_payment_timestamp)
                print(f"\n{name} added to database at {location}!")

            # If the customer name and location combination does already exist in the customers table, the user is notified.
            else:
                print(f"\n{name} already present at {location}!")


        # Option 2. Remove a customer       
        elif user_input == "2":

            # The customer name input from the prompt acts as the index into the customers table.
            name_to_remove = prompts.prompt_choose_customer(remove=True)

            # If the customer name does exist in the customers table, all entries in the customers table including the 
            # customer name are displayed.
            if database.customer_check(name_to_remove):
                customer_info = database.view_customer_info(name_to_remove)
                prompts.prompt_view_customers(f"\n{name_to_remove}'s Entries", customer_info)

                # The application loops until a valid, currently existing ID number is entered from the user.
                while True:

                    # The user is prompted for an ID number that exists in the customers table.
                    try:
                        entry_to_remove = prompts.prompt_choose_id(remove=True)

                        # If the ID number does exist in the customers table and it belongs to the selected customer, the 
                        # entry is removed from the table and the applications displays a confirmation message.
                        if database.id_check_customers(entry_to_remove, name_to_remove):
                            database.remove_customer(entry_to_remove, name_to_remove)
                            print(f"\n{entry_to_remove}. {name_to_remove} was removed from database!")
                            break

                    # If a non-integer is inputted from the user, the application loops again.
                    except ValueError:
                        continue
            
            # If the customer name does not exist in the customers table, the user is notified.
            else:
                print(f"\n{name_to_remove} isn't a current customer!")


        # Option 3. View customer(s)
        elif user_input == "3":

            # The application displays all entries in the customers table.
            all_customers = database.view_customers()
            prompts.prompt_view_customers("All Customers", all_customers)


        # Option 4. View customers who currently have late payments
        elif user_input == "4":

            # The application displays all entries in the customers table that currently late on their current payment,
            # (> 3o days late).
            late_customers = database.view_late_customers()
            prompts.prompt_view_customers("Late Customers", late_customers)


        # Option 5. Update a customer's last payment made
        elif user_input == "5":

            # The customer name input from the prompt acts as the index into the customers table.
            name_to_update = prompts.prompt_choose_customer(update=True)

            # If the customer name exists in the customers table, all entries in the customers table including the 
            # customer name are displayed.
            if database.customer_check(name_to_update):
                customer_info = database.view_customer_info(name_to_update)
                prompts.prompt_view_customers(f"{name_to_update}'s Entries", customer_info)

                # The application loops until a valid, currently existing ID number is entered from the user.
                while True:
                    try:
                        entry_to_update = prompts.prompt_choose_id(update=True)

                        # If the ID number does exist in the customers table and it belongs to the selected customer, the 
                        # user is prompted to update the entry's last payment date.
                        if database.id_check_customers(entry_to_update, name_to_update):
                            last_payment_timestamp, last_payment_date = prompts.prompt_update_last_payment()
                            database.update_last_payment(last_payment_timestamp, entry_to_update)

                            # Once the last payment date is updated, the application displays a confirmation message.
                            print(f"{name_to_update}'s last payment was updated to {last_payment_date}!")
                            break

                    # If a non-integer is inputted from the user, the application loops again.
                    except ValueError:
                        print("Invalid id selected!")
            
            # If the customer name does not exist in the customers table, the user is notified.
            else:
                print(f"\n{name_to_update} isn't a current customer!")


        # Option 6. Add a product
        elif user_input == "6":

            # The user inputs from the prompt act as the fields that will be inserted into the products table.
            product, product_type, price = prompts.prompt_add_product()

            # If the product name and  price combination does not already exist in the customers table, the customer
            # entry is added to the products table and the application displays a confirmation message.
            if not database.product_and_price_check(product, price):
                database.add_new_product(product, product_type, price)
                print(f"\n{product} added to database!")

            # If the product name and price combination does already exist in the customers table, the user is notified.
            else:
                print(f"\n{product_type}: {product} already in database!")


        # Option 7. Remove a product
        elif user_input == "7":

            # The product name input from the prompt acts as the index into the products table.
            product_to_remove = prompts.prompt_choose_product(remove=True)

            # If the product name does exist in the products table, all entries in the products table including the 
            # product name are displayed.
            if database.product_check(product_to_remove):
                product_info = database.view_product_info(product_to_remove)
                prompts.prompt_view_products(f"{product_to_remove}'s Entries", product_info)

                # The application loops until a valid, currently existing ID number is entered from the user.
                while True:
                    try:
                        entry_to_remove = int(input("Choose entry to remove (id): "))

                        # If the ID number does exist in the products table and it belongs to the selected customer, the 
                        # entry is removed from the table and the applications displays a confirmation message.
                        if database.id_check_products(entry_to_remove, product_to_remove):
                            database.remove_product(entry_to_remove, product_to_remove)
                            print(f"{product_to_remove} entry #{entry_to_remove} was removed from database!")
                            break

                    # If a non-integer is inputted from the user, the application loops again.
                    except ValueError:
                        continue

            # If the product name does not exist in the products table, the user is notified.
            else:
                print(f"{product_to_remove} isn't a current product!")


        # Option 8. View product(s)
        elif user_input == "8":

            # The application displays all entries in the products table.
            all_products = database.view_products()
            prompts.prompt_view_products("All Products", all_products)
        

        # Option 9. Edit the price of a product
        elif user_input == "9":

            # The product name input from the prompt acts as the index into the products table.
            product_to_update = prompts.prompt_choose_product(update=True)

            # If the product name exists in the products table and it belongs to the selected product, all entries in the 
            # products table including the product name are displayed.
            if database.product_check(product_to_update):
                product_info = database.view_product_info(product_to_update)
                prompts.prompt_view_products(f"{product_to_update}'s Entries", product_info)

                # The application loops until a valid, currently existing ID number is entered from the user.
                while True:
                    try:
                        entry_to_update = prompts.prompt_choose_id(update=True)

                        # If the ID number does exist in the products table , the user is prompted to update the entry's
                        # last payment date.
                        if database.id_check_products(entry_to_update, product_to_update):
                            price = prompts.prompt_update_price()
                            database.update_price(price, entry_to_update)

                            # Once the product price is updated, the application displays a confirmation message.
                            print(f"{product_to_update}'s price was updated to ${price}!")
                            break

                    # If a non-integer is inputted from the user, the application loops again.
                    except ValueError:
                        print("Invalid id selected!")

            # If the product name does not exist in the products table, the user is notified.
            else:
                print(f"{product_to_update} isn't a current product!")


        # Option 10. Assign a product to a customer
        elif user_input == "10":
            try:
                # The application will loop will continue until the user enters a valid, non-existing product assignment.
                while True:

                    # The application displays all entries in the customers table.
                    all_customers = database.view_customers()
                    prompts.prompt_view_customers("All Customers", all_customers)

                    # The user inputs from the prompt act as the fields that will be inserted into the products table from the customer
                    # table.
                    # NOTE: Only existing customer name and location combinations will work.
                    customer_to_assign, location_to_assign = prompts.prompt_add_customer_name_location()

                    # If the given customer name and location combination exists in the customers table, the combination is stored to
                    # be added to the customer_products table depending on if the user enters an existing product name and price 
                    # combination next.
                    if database.customer_at_location_check(customer_to_assign, location_to_assign):
                        
                        # The application displays all entries in the products table.
                        all_products = database.view_products()
                        prompts.prompt_view_products("All Products", all_products)

                        # The user inputs from the prompt act as the fields that will be inserted into the products table from the customer
                        # table.
                        # NOTE: Only existing product name and price combinations will work.
                        product_to_assign, price_to_assign = prompts.prompt_add_product_name_price()
                        
                        # If the given customer name and location combination exists in the customers table, the combination is stored to
                        # be added to be added to the customer_products table.
                        if database.product_and_price_check(product_to_assign, price_to_assign):
                            break
                        
                
                # If the product assignment does not already exist in the customer_products table, then the assignment in then added to the table.
                database.assign_product_to_customer(customer_to_assign, location_to_assign, product_to_assign, price_to_assign)
                print(f"{product_to_assign} assigned to {customer_to_assign} at {location_to_assign}!")

            # If a product assignment already exists, then the user is notified.
            except sqlite3.IntegrityError:
                print(f"{product_to_assign} is already assigned to {customer_to_assign} at {location_to_assign}!")


        # 11. Unassign a product from a customer
        elif user_input == "11":

            # The product assignment ID input from the prompt acts as the index into the customer_products table.
            assignment_to_remove = prompts.prompt_remove_assignment()

            # If the product assignment ID exists in the customer_products table, the product assignment is removed from the table
            # and the application displays a confirmation message.
            if database.id_check_customer_products(assignment_to_remove):
                database.remove_assignment(assignment_to_remove)
                print("Product unassigned from customer.")

            # If the product assignment ID does not exist in the customer_products table, the user is notified.
            else:
                print("This id does not identify a current product assignment!")


        # Option 12. View product assignment(s)
        elif user_input == "12":

            # The application displays all entries in the customer_products table.
            all_assignments = database.view_assignments()
            prompts.prompt_view_assignments("All Product Assignments", all_assignments)


        # Option 13. View a customer's monthly bill
        elif user_input == "13":
            while True:

                # The customer name input from the prompt acts as the index into the customer_products table.
                name_to_view = prompts.prompt_choose_customer(bill=True)

                # If the customer is assigned to at least one product, the user's monthly bill is diplayed.
                if database.customer_assignment_check(name_to_view):
                    bill = database.view_monthly_bill(name_to_view)
                    prompts.prompt_view_monthly_bill(f"{name_to_view}'s Monthly Bill", bill)
                    break

                # If the customer is not assigned to at least one product, the user is notified.
                else:
                    print(f"{name_to_view} does not have any current products assigned to them!")
        

        # Any input outside of the valid options results in this error message.
        else:
            print("\nInvalid selection! Enter a valid selection.")


    # When the user inputs "14", the exit message with print and the program will exit
    print("\nExiting Data Plus Fiber's customer tracking system. Goodbye!")


# If the user exits out of the program using Keyboard Interrupt, the same exit message will print
except KeyboardInterrupt:
    print("\nExiting Data Plus Fiber's customer tracking system. Goodbye!")