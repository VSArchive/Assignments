import re

string = "jutcxtuexcviajjib"

match1 = re.search('a', string)
match2 = re.search('b$', string)

if match1:
    print("Pattern has", match1.group())
if match2:
    print("Pattern ends with", match2.group())
else:
    print("Dose not contain a and ends with b")
