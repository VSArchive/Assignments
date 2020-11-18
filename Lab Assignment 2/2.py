d = {}

for i in range(1, 21):
    d.update({i: i * i})

x = 0
y= []

for i in range(1, 21):
    x += d[i]
    y.append(d[i])

print("Sum is :",x)
print("Maximum is :",max(y))
print("Minimum is :",min(y))
