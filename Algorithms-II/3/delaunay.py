# Imports
import matplotlib.pyplot as plt
import numpy as np
import random

# initialize the points
points = []

x = 100
y = 100
no_of_cells = 10

# generate random points
for i in range(no_of_cells):
    points.append([random.randint(0, x), random.randint(0, y)])

# initialize an empty image
img = np.array(np.zeros((x, y)))


# calculate the distance between each point and each other point
def hypot(p1, p2):
    return (p1**2+p2**2)**0.5


delaunay_points = {}


# for pixels
for i in range(x):
    for j in range(y):

        # set a initial value for the minimum distance from origin
        min = hypot(x-1, y-1)
        n = -1
        nk = []

        # for all points
        for k in range(no_of_cells):
            d = hypot(points[k][0]-j, points[k][1]-i)
            # if the distance is smaller than the minimum distance
            if d < min:
                # set the minimum distance to the new distance
                min = d
                n = k
                nk = points[k]

        if n != -1:
            # set the pixel to the color of the point
            img[i][j] = n
            delaunay_points[n] = nk

arr = list(delaunay_points.keys())

for n in range(len(delaunay_points.values())):
    try: 
        adj = []
        for i in range(delaunay_points[n][0], x):
            br = False
            for j in range(delaunay_points[n][1], y):
                if arr[n] != img[i][j] and not adj.__contains__(int(img[i][j])):
                    adj.append(int(img[i][j]))
                    br = True
                    break
            if br:
                break

        for i in range(delaunay_points[n][0], 0, -1):
            br = False
            for j in range(delaunay_points[n][1], 0, -1):
                if arr[n] != img[i][j] and not adj.__contains__(int(img[i][j])):
                    adj.append(int(img[i][j]))
                    br = True
                    break
            if br:
                break
                
        for i in range(delaunay_points[n][0], x):
            br = False
            for j in range(delaunay_points[n][1], 0, -1):
                if arr[n] != img[i][j] and not adj.__contains__(int(img[i][j])):
                    adj.append(int(img[i][j]))
                    br = True
                    break
            if br:
                break

        for i in range(delaunay_points[n][0], 0, -1):
            br = False
            for j in range(delaunay_points[n][1], y):
                if arr[n] != img[i][j] and not adj.__contains__(int(img[i][j])):
                    adj.append(int(img[i][j]))
                    br = True
                    break
            if br:
                break

        print(arr[n], adj)

        a = []
        b = []
        for i in adj:
            # print(delaunay_points[i])
            a.append(delaunay_points[i][0])
            b.append(delaunay_points[i][1])

        a.append(a[0])
        b.append(b[0])

        plt.plot(a, b)
    except:
        pass
    # break


x = [x[0] for x in points]
y = [x[1] for x in points]
plt.plot(np.array(x), np.array(y), 'o')
# x = [x[0] for x in points]
# y = [x[1] for x in points]
# plt.plot(np.array(x), np.array(y))
plt.imshow(img)
plt.show()
