import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"^[A-Za-z]+([\-']?[A-Za-z]+)?( [A-Za-z]+([\-']?[A-Za-z]+)?)*$"
name_regex = re.compile(name)

phone_number = r"^(\+1\s?)?(\(?\d{3}\)?[\s.-]?)\d{3}[\s.-]?\d{4}$"
phone_regex = re.compile(phone_number)

email_address = r""
email_regex = re.compile(email_address)
