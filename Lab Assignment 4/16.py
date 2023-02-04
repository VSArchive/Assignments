import re

data = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]

for i in data:
    match = re.split('[(]', i)
    print(match[0])