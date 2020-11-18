string = input("Enter A String : ")

str1 = string.split()
str2 = []

for i in str1:

    if i not in str2:
        str2.append(i)

for i in range(0, len(str2)):
    print('Frequency of', str2[i], ' :', str1.count(str2[i]))
