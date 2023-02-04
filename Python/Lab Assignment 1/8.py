string = input("Enter A String : ")

str1 = list(string)
str2 = []

for i in str1:

    if i not in str2:
        str2.append(i)

for i in range(0, len(str2)):
    if str1.count(str2[i]) == 1:
        print(str2[i])
        break
