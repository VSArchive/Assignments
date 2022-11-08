# Items
#   weight, value
items = [
    (15, 30),
    (10, 25),
    (2, 2),
    (4, 6),
]

# Knapsack capacity
W = 37

# Number of items
n = len(items)

# Sort items by value/weight ratio
items = sorted(items, key=lambda x: x[1]/x[0], reverse=True)

# Compute upper bound
def upper_bound(i, w, v):
    global items, W, n
    if w >= W:
        return 0
    b = v
    j = i
    while j < n and w + items[j][0] <= W:
        w += items[j][0]
        b += items[j][1]
        j += 1
    if j < n:
        b += (W-w) * items[j][1] / items[j][0]
    return b

# Branch and bound algorithm
def knapsack():
    global items, W, n
    best = 0
    best_set = []
    stack = [(0, 0, 0, [])]
    while len(stack) > 0:
        i, w, v, s = stack.pop()
        if w <= W and v > best:
            best = v
            best_set = s
        if i < n and upper_bound(i, w, v) > best:
            stack.append((i+1, w+items[i][0], v+items[i][1], s+[i]))
            stack.append((i+1, w, v, s))
    return best, best_set

best, best_set = knapsack()
print(f'Best value: {best}')
print(f'Best set: {best_set}')
