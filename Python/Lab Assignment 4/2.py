import re

string = "abscc"

match = re.search('a?b', string)

if match:
    print("There is b followed by a")
    print(match.group())
else:
    print("No b followed by a")
