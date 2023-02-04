file = open("expr.txt", "r")

for i in file:
    print(eval(i))
