import re

string = "Clearly, he has no excuse for such behavior."

match = re.finditer(r"\w+ly", string)

for m in match:
    print(m.start(), m.end(), m.group(0))
