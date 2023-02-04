# points = [
#     [0, 3],
#     [2, 2],
#     [1, 1],
#     [2, 1],
#     [3, 0],
#     [0, 0],
#     [3, 3]
# ]

# Take length of points as input
n = int(input("Enter the number of points: "))
# points array to store all points
points = []


# for in length of points take x and y as input
for i in range(n):
    x = int(input(f"Enter x coordinate of point {i+1}: "))
    y = int(input(f"Enter y coordinate of point {i+1}: "))
    # append x and y to points array
    points.append([x, y])

# if points are lessthan 3 print array
if n < 3:
    print(points)
    exit()


# check if points
def ccw(x, y, z):
    return ((z[0] - y[0]) * (y[1] - x[1])) - ((y[0] - x[0]) * (z[1] - y[1])) > 0


# initially take leftmost as 0
left_most = 0

# then search the leftmost point wrt x axis
for i in range(1, n):
    if points[i][0] < points[left_most][0]:
        left_most = i

polygon = []

p = int(left_most)
q = 0

while True:
    polygon.append(p)

    # go to next point in array if its the last go to start
    if p+1 < n:
        q = (p+1)
    else:
        q = 0

    # For All i find in CCW
    for i in range(n):
        if (ccw(points[p], points[i], points[q])):
            q = i

    p = q

    # if came back to start break
    if p == left_most:
        break

# print selected points
for i in polygon:
    print(points[i])
