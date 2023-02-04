import random

arr = []


def knapSack(limit, wt, val, n):
    if n == 0 or limit == 0:
        return 0
    if (wt[n-1] > limit):
        return knapSack(limit, wt, val, n-1)
    else:
        max_object = max(val[n-1] + knapSack(limit-wt[n-1],
                         wt, val, n-1), knapSack(limit, wt, val, n-1))
        if max_object == (val[n-1] + knapSack(limit-wt[n-1], wt, val, n-1)):
            print("Current Selected :", wt[n-1], end="\n ... next loop ... \n")
            arr.append(wt[n-1])
        else:
            print("Current Selected :", wt[n], end="\n ... next loop ... \n")
            arr.append(wt[n])
        return max_object


# val = [50, 60, 70, 80, 90, 100]
# wt = [10, 20, 30, 40, 50, 60]

val = []
wt = []

limit = random.randint(10, 100)

for i in range(6):
    val.append(random.randint(50, 100))
    wt.append(random.randint(10, 60))


print("Input Value Array :", val)
print("Input Weight Array :", wt)
print("Input Limit :", limit)

n = len(val)

out = knapSack(limit, wt, val, n)
print("Final Selected Weights: ", arr[len(arr)-1:len(arr)-3:-1])
print("Output is :", out)
