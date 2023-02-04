import math

import matplotlib.pyplot as plt

g1 = []
g2 = []
y = []

x = 1
z = 1


def eq(n, t):
    global x, z
    y.append(t)
    for j in range(1, n):
        z = (2 ** n) * math.factorial(n)
        x = x + (t ** (2 * j)) / z
    return x


for i in range(1, 10):
    x = eq(2, i)
    print(x, end=" ")
    g1.append(x)

print('\n')

x = 1
z = 1
y.clear()

for i in range(1, 10):
    x = eq(3, i)
    print(x, end=" ")
    g2.append(x)

print('\n')

plt.plot(y, g1)
plt.plot(y, g2)

plt.show()
