import re

string = "wer345678reko98765yu"

match = re.split('[a-z]|[A-Z]', string)

j = 0
for i in match:
    if i != "":
        print("Number " + i + " Position " + str(j))

    j += 1