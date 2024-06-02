import re
def validate_email(email):
    pattern=r"^[a-zA-Z0-9_.+_]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9_.]+$"
    match=re.match(pattern,email)
    return match is not None
email1="john@example.com"
email2="invalid_email"
print(validate_email(email1))
print(validate_email(email2))

import re
def validate_phone_number(phone_number):
    pattern=r"^\d{3}-\d{3}-\d{4}$"
    match=re.match(pattern,phone_number)
    return match is not None
phone1="123-456-7890"
phone2="9844387103"
print(validate_phone_number(phone1))
print(validate_phone_number(phone2))

#validating Dates in YYYY-MM-DD format
import re
def validate_date(date):
    pattern=r"^\d{4}-\d{2}-\d{2}$"
    match=re.match(pattern,date)
    return match is not None
#example usage
date1="2022-05-20"
date2="05-20-2022"
print(validate_date(date1))
print(validate_date(date2))

import re
def validate_password(password):
    pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
    match=re.match(pattern,password)
    return match is not None

password1="Password123"
password2="weakpassword"
print(validate_password(password1))
print(validate_password(password2))
