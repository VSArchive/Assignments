import re

patterns = ['fox', 'dog', 'horse']

string = 'The quick brown fox jumps over the lazy dog.'

for i in patterns:
    match = re.search(i, string)
    if match:
        print("Found", match.group())
    else:
        print("Not Found", i)
