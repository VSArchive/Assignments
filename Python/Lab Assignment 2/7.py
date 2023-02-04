x = input("Enter string : ")

d1 = {}

for i in x:
    if i in d1.keys():
        d1.update({i: d1[i] + 1})
    else:
        d1.update({i: 1})

for i in d1:
    if d1[i] == 1:
        print(i)
        break
