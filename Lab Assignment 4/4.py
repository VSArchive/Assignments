import re

string = "AAabscc"

match = re.search('[A-Z]+[a-z]+$', string)

if match:
    print("There are upper case letter followed by lower")
    print(match.group())
else:
    print("There no are upper case letter followed by lower")
