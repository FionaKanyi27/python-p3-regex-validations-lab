import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"^([A-Z][a-z]*(['\-][A-Z][a-z]+)?)( [A-Z][a-z]*(['\-][A-Z][a-z]+)?)*$"
name_regex = re.compile(name)

phone_number = r"^(\+1\s?)?(\(?\d{3}\)?[\s.-]?)\d{3}[\s.-]?\d{4}$"
phone_regex = re.compile(phone_number)

email_address = r"^[A-Za-z][\w\.-]*@[A-Za-z0-9-]+\.[A-Za-z]{2,}$"
email_regex = re.compile(email_address)
