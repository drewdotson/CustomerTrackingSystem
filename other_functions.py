
# NOTE: This file contains functions that didn't belong anywhere else in the application. It consists of two
# validation functions to enforce the desired format of phone numbers and dates.

import re

# VALIDATION FUNCTIONS 👇 ---------------------------------------------------------------------------------------#

# Function used to validate if a phone number input for a customer is of the correct format.
def valid_phone_number(phone_num):
    format = re.compile(r"^\d{3}-\d{3}-\d{4}$")
    if format.match(phone_num):
        return True
    else:
        return False

# Function used to validate if the date inputs for a customer are in the correct format.
def valid_date(date):
    format = r"^(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])-\d{4}$"
    if re.match(format, date):
        return True
    else:
        return False