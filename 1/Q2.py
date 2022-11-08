# p1
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# p2
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# p3
x3 = float(input("Enter x3: "))
y3 = float(input("Enter y3: "))

print("1. Point on line")
print("2. Point on line segment")

method = int(input("Enter method: "))

if method == 1:
    # if slope of p1, p2 is same as slope of p1, p3 on same line
    if ((x2-x1)/(y2-y1)) == ((x3-x1)/(y3-y1)):
        print("The points are on the same line")
    else:
        print("The points are not on the same line")

elif method == 2:
    # if distance of p1, p2 is same as distance of p1, p3 + distance of p3, p2
    if ((x2 - x1)**2 + (y2 - y1)**2)**0.5 == (((x3 - x2)**2 + (y3 - y2)**2)**0.5 + ((x3 - x1)**2 + (y3 - y1)**2))**0.5:
        print("The points are on the line segment")
    else:
        print("The points are not on the line segment")
