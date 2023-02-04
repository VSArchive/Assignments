file = open("f1.txt", "r")
feven = open("even.txt", "a")
fodd = open("odd.txt", "a")

j = 0

for i in file:
    if j % 2 != 0:
        feven.write(i)
    if j % 2 == 0:
        fodd.write(i)

    j += 1
