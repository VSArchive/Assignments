a = []

for i in range(10):
    a.append(int(input("Enter element of Array : ")))

max = 0
num = 0

for i in range(0, len(a)):
    num += a[i]
    if max < num:
        max = num

    if num < 0:
        num = 0

print("Maximum sum is : ", max)
