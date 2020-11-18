import re

string = 'The quick brown fox jumps e over wf the lazy dog'

match1 = re.split(' ', string)

x = int(input("Enter Number : "))

pattern = ""

for i in range(x, 1, -1):
    for j in range(i):
        pattern += "[A-z]"
    pattern += "|"

pattern += "[A-z]"

for i in match1:
    match2 = re.search(pattern, i)
    if match2:
        if match2.group() != i:
            print(i)
