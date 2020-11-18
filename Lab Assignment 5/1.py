import random

KM = input().split(" ")

K = int(KM[0])
M = int(KM[1])

lists = []
y = []

for i in range(K):
    x = input().split(" ")
    y.append(int(x.pop(0)))
    lists.append(x)

S1 = 0
S2 = 0

for i in range(len(lists)):
    for j in range(len(lists[i])):
        lists[i][j] = int(lists[i][j]) ** 2

for i in range(len(lists)):
    S1 += max(lists[i])

if S1 < M:
    print(S1 % M)

else:
    z = 1
    q = []
    for m in y:
        z *= m
    for c in range(z):
        for i in range(len(lists)):
            j = random.randint(0, len(lists[i]) - 1)
            S2 += lists[i][j]
        q.append(S2 % M)
        S2 = 0

    print(max(q))

# 3 1000
# 2 5 4
# 3 7 8 9
# 5 5 7 8 9 10
