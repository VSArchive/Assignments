import re

string = "ihwehfvkdjlihugs$#EWsasih4r8784q&#*(&8798&&^(*&*^%(*&("

match = re.findall('[a-z]|[A-Z]|[0-9]', string)

for i in match:
    print(i, end="")
