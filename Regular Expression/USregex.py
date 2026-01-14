import re

pattern = re.compile(r'^(?:\+1\s?)?(?:\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}$')

phone = input("Enter a US phone number: ")

if pattern.match(phone):
    print("Valid US phone number")
else:
    print("Invalid US phone number")