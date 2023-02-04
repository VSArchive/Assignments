a = str(input("Enter first string : "))
b = str(input("Enter second string : "))

x = list(a)
y = list(b)

if x.sort() == y.sort():
    print("anagram")

else:
    print("not anagram")
