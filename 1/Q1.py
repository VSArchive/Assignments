# p1
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# p2
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = float(input("Enter distance: "))

length = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# p3 = (1-distance/length)*p1 + distance/length*p2
# using ratio of distances
# x3 = (1 - (distance/length)) * x1 + (distance/length) * x2
# y3 = (1 - (distance/length)) * y1 + (distance/length) * y2

x3 = x1 + (distance/length) * (x2-x1)
y3 = y1 + (distance/length) * (y2-y1)

print(x3, y3)
