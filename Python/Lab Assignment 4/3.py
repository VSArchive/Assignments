import re

string = "abscc"

match = re.search('a?bb', string)
match1 = re.search('a?b', string)

if match:
    print("There are more than one b followed by a")
    print(match.group())
elif match1:
    print("There is b followed by a")
    print(match1.group())
else:
    print("No b followed by a")
