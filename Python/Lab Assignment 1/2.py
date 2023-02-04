x = int(input("Enter the Max Length : "))
a = int(input("Enter the first term : "))
b = int(input("Enter the second term : "))
if x == 1:
    print("0")
else:
    print(a)
    print(b)
    for i in range(2, x):
        c = a + b
        a = b
        b = c
        print(c)
