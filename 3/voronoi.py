from PIL import Image
import random

points = []

x = 100
y = 100
no_of_cells = 10
color = []

for i in range(no_of_cells):
    points.append([random.randint(0, x), random.randint(0, y)])
    color.append((random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255)))

image = Image.new("RGB", (x, y))
putpixel = image.putpixel


def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


for i in range(x):
    for j in range(y):
        min = distance(points[0], [i, j])
        n = -1

        for k in range(no_of_cells):
            d = distance(points[k], [i, j])
            if d < min:
                min = d
                n = k

        if n != -1:
            putpixel((i, j), color[n])

image.show()
