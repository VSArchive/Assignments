string = input("Enter A String : ")

str1 = list(string)
str2 = []
m = 1

for i in str1:
    try:
        str2.append(int(i))
        m = 0
    except ValueError:
        if m == 0:
            break
        continue

for i in str2:
    print(i, end="")
