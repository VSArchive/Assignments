import matplotlib.pyplot as plt

y = 1

y1 = []
y2 = []


def eq(n):
    global y
    y1.append(n)
    for i in range(1, n):
        y = y + 0.1 * y
    y2.append(y)
    print(y)


for i in range(1, 10):
    eq(i)

plt.plot(y1, y2)

plt.show()
