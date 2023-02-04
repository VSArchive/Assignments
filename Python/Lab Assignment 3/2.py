file = open("f1.txt", "r")
vowels = open("vowels.txt", "a")
cons = open("cons.txt", "a")

for i in file:
    if i[0] == "a" or i[0] == "e" or i[0] == "i" or i[0] == "o" or i[0] == "u":
        vowels.write(i)
    else:
        cons.write(i)
