d = {}
a = []

x = 0

while x != "-1":
    x = input("Enter Key : ")
    if x != "-1":
        y = input("Enter Value : ")
        a.append(y)
        d.update({x: y})

e = d.copy()

for i in d:
    if a.count(d[i]) > 1:
        e.pop(i)
    else:
        print(e[i])
