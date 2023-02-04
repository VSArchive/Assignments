import re

date = "2020-10-17"

match1 = re.split('-', date)

print(match1[2]+"-"+match1[1]+"-"+match1[0])
