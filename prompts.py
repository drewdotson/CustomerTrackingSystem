
# NOTE: This file contains all of the prompts used to gather user input for a multitude of different functions across
# the main file. This is the only file in the application that takes user input.

import other_functions
from datetime import datetime

# INSERT PROMPTS 👇 ---------------------------------------------------------------------------------------------#

# Prompt used for gathering customer information from user input
# Prompt takes a customer's name, phone number, location, card number, the date they signed
# up, and the last date they made a payment.
# NOTE: A customer can have multiple entries as long as their location is unique for each entry.
def prompt_add_customer():

    name = input("\nCustomer's name: ")

    phone_num = input("Phone number (XXX-XXX-XXXX format): ")
    # The application loops until the user enters a valid phone number in XXX-XXX-XXXX format.
    while not other_functions.valid_phone_number(phone_num):
            phone_num = input("Phone number (XXX-XXX-XXXX format): ")

    location = input("Location: ")

    card_num = input("Customer's card number (enter number with no dashes): ")
    # The application loops until the user enters a valid card number length.
    while len(card_num) < 13 or len(card_num) > 19:
        card_num = input("Customer's card number (enter number with no dashes): ")
    
    sign_up = input("Customer sign-up date (mm-dd-YYYY): ")
    # The application loops until the user enters a valid date in mm-dd-YYYY format.
    while not other_functions.valid_date(sign_up):
            sign_up = input("Customer sign-up date (mm-dd-YYYY): ")

    # The sign up date is converted into a timestamp in order to be used properly in SQLite queries.
    sign_up_date = datetime.strptime(sign_up, "%m-%d-%Y")
    sign_up_timestamp = sign_up_date.timestamp()

    last_payment = input("Date of last payment (mm-dd-YYYY): ")
    # The application loops until the user enters a valid date in mm-dd-YYYY format.
    while not other_functions.valid_date(last_payment):
            last_payment = input("Date of last payment (mm-dd-YYYY): ")

    # The last payment date is converted into a timestamp in order to be used properly in SQLite queries. 
    last_payment_date = datetime.strptime(last_payment, "%m-%d-%Y")
    last_payment_timestamp = last_payment_date.timestamp()

    # The prompt returns the inputs which will be used to fill the corresponding fields in the customers 
    # table.
    return name, phone_num, location, str(card_num), sign_up_timestamp, last_payment_timestamp


# Prompt used for gathering product information from user input
# Prompt takes a product's name, if that product is a piece of equipment or a service, and
# its setup price (if equipment) / monthly fee (if service).
def prompt_add_product():

    product = input("\nProduct's name: ")

    product_type =  input("Equipment or Service: ").strip().lower()
    # The application loops until a valid product type is entered.
    while True:
        if product_type == "equipment" or product_type == "service":
            break
        else:
            product_type =  input("Equipment or Service: ").strip().lower()

    # If the product is a piece of equipment, the price is set to $0 as the equipment is complementary.
    if product_type == "equipment":
        price = 0

    # If the product is a service, then the user must manually enter the product's monthly fee.
    else:

        # The application loops until a floating point number is entered. 
        while True:
            try:
                price = round((float(input("Service monthly fee: $"))), 2)
                break
            except ValueError:
                print("Enter a number!")

    # The prompt returns the inputs which will be used to fill the corresponding fields in the products 
    # table.
    return product, product_type.capitalize(), price


# Prompt used for gathering customer information from user input to add to customer_products table.
# Prompt takes a customer's name and location as input
def prompt_add_customer_name_location():
    
    customer_to_assign = input("Enter customer name: ")
    location_to_assign = input("Enter customer's location: ")

    return customer_to_assign, location_to_assign


# Prompt used for gathering customer information from user input to add to customer_products table.
# Prompt takes a customer's name and location as input
def prompt_add_product_name_price():
    
    product_to_assign = input("Choose product to assign to customer: ")
    
    # The application loops until a floating point number is entered. 
    while True:
        try:
            price_to_assign = round((float(input("Choose a price to assign to customer: "))), 2)
            break

        # If a non-integer is inputted from the user, the application loops again.
        except ValueError:
            print("Enter a number!")

    return product_to_assign, price_to_assign

# VIEW PROMPTS 👇 -----------------------------------------------------------------------------------------------#

# Prompt used to view customers in database. What customers are returned depend on the option selected by the user.
def prompt_view_customers(title, customers):
    print(f"\n🛜------{title}-----🛜")
    for id, name, phone_num, location, card_num, sign_up_timestamp, last_payment_timestamp in customers:

        # Process to convert the last payment timestamp back into the proper mm-dd-YYYY format.
        sign_up_object = datetime.fromtimestamp(sign_up_timestamp)
        sign_up_date = sign_up_object.strftime("%b %d %Y")

        # Process to convert the last payment timestamp back into the proper mm-dd-YYYY format.
        last_payment_object = datetime.fromtimestamp(last_payment_timestamp)
        last_payment_date = last_payment_object.strftime("%b %d %Y")

        print(f"{id}. | Name: {name} | Phone: {phone_num} | Address: {location} | Card: {card_num} | Joined: {sign_up_date} | Last Payment: {last_payment_date}")
    print("---------------------------")


# Prompt used to view products in database. What customers are returned depend on the option selected by the user.
def prompt_view_products(title, products):
    print(f"\n🛜------{title}-----🛜")
    for id, product, product_type, price in products:
        print(f"{id}. | Name: {product} | Type: {product_type} | Price: {price}")
    print("---------------------------")


# Prompt used to view product assignments in database.
def prompt_view_assignments(title, assignments):
    print(f"\n🛜------{title}-----🛜")
    for id, customer_name, customer_location, product_name, product_price in assignments:
        print(f"{id}. | Name: {customer_name} | Location: {customer_location} | Product: {product_name} | Price: {product_price}")
    print("---------------------------")


# Prompt used to view a specified customer's monthly bill.
def prompt_view_monthly_bill(title, bill):
    print(f"\n🛜------{title}-----🛜")
    for bill in bill:
        print(f"💵------------${bill[0]}----------💵")
    print("---------------------------------")

# DELETE / UPDATE PROMPTS 👇 ----------------------------------------------------------------------------------#

# Prompt used to choose a customer to remove from the database, to have their last payment date updated, or to
# have their monthly bill displayed.
def prompt_choose_customer(remove=False, update=False, bill=False):

    if remove:
        name = input("\nEnter name of customer to remove: ")
        return name
    
    elif update:
        name = input("\nEnter name of customer to update last made payment: ")
        return name
    
    elif bill:
        name = input("\nEnter name of customer to view monthly bill: ")
        return name


# Prompt used to update a customer's last made payment.
def prompt_update_last_payment():

    last_payment = input("\nDate of last payment (mm-dd-YYYY): ")
    # The application loops until the user enters a valid date in mm-dd-YYYY format.
    while not other_functions.valid_date(last_payment):
            last_payment = input("Date of last payment (mm-dd-YYYY): ")

    # The new last payment date is converted into a timestamp in order to be used properly in SQLite queries.
    last_payment_date = datetime.strptime(last_payment, "%m-%d-%Y")
    last_payment_timestamp = last_payment_date.timestamp()

    # The last payment date is also updated to a string in a seperate variable which will be used in the print
    # statement when a last payment date is updated.
    last_payment_date = last_payment_date.strftime("%m-%d-%Y")

    # The newly updated last payment date timestamp is returned.
    return last_payment_timestamp, last_payment_date


# Prompt used to choose a product either to remove from the products table. or to have its price updated.
def prompt_choose_product(remove=False, update=False):

    if remove:
        name = input("\nEnter name of product to remove: ")
        return name
    
    elif update:
        name = input("\nEnter name of product to update price: ")
        return name


# Prompt used to update a product's price.
def prompt_update_price():
    print("")

    # The application loops until a floating point number is entered
    while True:
        try:
            price = round((float(input("New price of product ($): "))), 2)
            break
        except ValueError:
            print("Enter a number!")

    # The newly updated product price is returned.
    return price


# Prompt used to choose a product assignment to remove from the customer_products table.
def prompt_remove_assignment():

    #  The application loops until an integer is entered.
    while True:

        try:
            id = int(input("\nEnter assignment to remove (id): "))
            break

        except ValueError:
            print("Enter a number!")

    return id


# Prompt used to choose entry ID for a multitude of functions spanning all 3 tables of the database.
def prompt_choose_id(remove=False, update=False):

    if remove:
        id = int(input("\nChoose entry to remove (id): "))
        return id
    
    elif update:
        name = int(input("Choose entry to update (id): "))
        return name
