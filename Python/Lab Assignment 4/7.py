import re

string = "sdfghdsrthgfdes865r"

match = re.search('[0-9][0-9][0-9]|[0-9][0-9]|[0-9]', string)

if match:
    print("Has numbers (0-9) of length between 1 to 3", match.group())
else:
    print("Dose not have a number")
