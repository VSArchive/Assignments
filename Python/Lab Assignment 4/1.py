import re

string = "jljsdrvjbszd@$#"

match = re.match('^[a-zA-Z0-9]+$', string)

if match:
    print("Alpha Numerical")
    print(match.group())
else:
    print("Not Alpha Numerical")
