import re

string = 'The quick brown fox jumps e over wf the lazy dog.'

match1 = re.split(' ', string)

# print(match1)
for i in match1:
    match2 = re.search('[A-z][A-z][A-z][A-z][A-z]|[A-z][A-z][A-z][A-z]|[A-z][A-z][A-z]', i)
    if match2:
        if match2.group() == i:
            print(match2.group())
