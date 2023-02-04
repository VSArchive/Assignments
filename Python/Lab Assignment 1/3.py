x = int(input("Enter the Number : "))
if x == 0:
    print("1")
else:
    fact = 1
    if x < 0:
        x = x*-1
    for i in range(1, x + 1):
        fact = fact * i
    print(fact)
