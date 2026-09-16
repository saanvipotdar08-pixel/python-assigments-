import re

string = input("Enter a string: ")

pattern = "^[a-zA-Z0-9]+$"

if re.match(pattern, string):
    print("The string contains only letters (a-z, A-Z) and digits (0-9).")
else:
    print("The string contains invalid characters.")