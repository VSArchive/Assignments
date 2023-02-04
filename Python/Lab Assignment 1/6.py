num = str(input("Enter num : "))

for i in range(len(num)):
    if num[i] == num[len(num) - 1 - i]:
        print("Palindrome")
    else:
        print("Not Palindrome")
        break
