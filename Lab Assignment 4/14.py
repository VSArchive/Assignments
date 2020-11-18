import re

decimal = '123.11'

match = re.search("^[0-9]+(\.[0-9]{1,2})?$", decimal)

if match:
    print("Is Decimal")
else:
    print("Not decimal")