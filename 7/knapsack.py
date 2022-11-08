import random

arr = []

# store the nodes of recursion tree
storage = {}

# recurssion 
def knapSack(limit, wt, val, n):
    # if reached end of recursion tree return 0
    if n == 0 or limit == 0:
        return 0

    if (wt[n-1] > limit):
        lim2 = 0
        if storage.get(f"{limit}-{n-1}"):
            print("Used From Storage")
            lim2 = storage[f"{limit}-{n-1}"]
        else:
            lim2 = knapSack(limit, wt, val, n-1)
            storage[f"{limit}-{n-1}"] = lim2
        return lim2
    else:
        lim1 = 0
        lim2 = 0
        # if the node is already visited return the value
        if storage.get(f"{limit-wt[n-1]}-{n-1}"):
            print("Used From Storage")
            lim1 = storage[f"{limit-wt[n-1]}-{n-1}"]
        else:
            lim1 = knapSack(limit-wt[n-1],
                     wt, val, n-1)
            storage[f"{limit-wt[n-1]}-{n-1}"] = lim1

        # if the node is already visited return the value
        if storage.get(f"{limit}-{n-1}"):
            print("Used From Storage")
            lim2 = storage[f"{limit}-{n-1}"]
        else:
            # if not visited then visit the node
            lim2 = knapSack(limit, wt, val, n-1)
            storage[f"{limit}-{n-1}"] = lim2
        
        max_object = max(val[n-1] + lim1, lim2)

        # save the node to find the last elements of node which will be the selected node of the knapsack
        if max_object == (val[n-1] + lim1):
            print("Current Selected :", wt[n-1], end="\n ... next loop ... \n")
            arr.append(f"Weight : {wt[n-1]}, Value : {val[n-1]}")
        else:
            print("Current Selected :", wt[n], end="\n ... next loop ... \n")
            arr.append(f"Weight : {wt[n]}, Value : {val[n]}")
        return max_object


# val = [1, 6, 10, 16]
# wt = [1, 2, 3, 5]
# limit = 50

val = []
wt = []

# generate random values for limit
limit = random.randint(10, 100)

# generate random values for val and wt
for i in range(6):
    val.append(random.randint(50, 100))
    wt.append(random.randint(10, 60))


print("Input Value Array :", val)
print("Input Weight Array :", wt)
print("Input Limit :", limit)


n = len(val)

# call the function and print the result
out = knapSack(limit, wt, val, n)
print("Storage :", storage)
print("Final Selected Weights: ", arr[len(arr)-1:len(arr)-3:-1])
print("Output is :", out)
