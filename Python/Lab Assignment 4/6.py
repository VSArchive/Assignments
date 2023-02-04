import re

string = "zjutcxtuexcviajjib"

match = re.search('\Az|z$', string)

if match:
    print("Pattern starts or ends with", match.group())
