x = input("Enter first string : ")
y = input("Enter second string : ")

d1 = {}
d2 = {}
anagram = True

for i in x:
    if i in d1.keys():
        d1.update({i: d1[i] + 1})
    else:
        d1.update({i: 1})

for i in y:
    if i in d2.keys():
        d2.update({i: d2[i] + 1})
    else:
        d2.update({i: 1})

for i in d1:
    if i in d2.keys():
        if d1[i] == d2[i]:
            continue
        else:
            print("Not an anagram")
            anagram = False
            break
    else:
        print("Not an anagram")
        anagram = False
        break

if anagram:
    print("anagram")
