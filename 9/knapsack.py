import random
import bisect

X = [0] * 1000
Y = [0] * 1000


def calcsubarray(val, x, n, c) -> None:
    for i in range((1 << n)):
        s = 0
        for j in range(n):
            if (i & (1 << j)):
                s += val[j + c]
        x[i] = s


def solveSubsetSum(val, n, limit) -> int:
    global Y

    calcsubarray(val, X, n // 2, 0)
    calcsubarray(val, Y, n - n // 2, n // 2)
    size_X = 1 << (n // 2)
    size_Y = 1 << (n - n // 2)

    YY = Y[:size_Y]
    YY.sort()
    Y = YY

    maximum = 0

    for i in range(size_X):
        if (X[i] <= limit):
            p = bisect.bisect_left(Y, limit - X[i])

            if (p == size_Y or (p < size_Y and Y[p] != (limit - X[i]))):
                p -= 1
            if ((Y[p] + X[i]) > maximum):
                maximum = Y[p] + X[i]
    return maximum


if __name__ == "__main__":

    val = []

    limit = random.randint(10, 40)

    for i in range(6):
        val.append(random.randint(1, 50))

    print("Input Value Array :", val)
    print("Input Limit :", limit)

    n = len(val)

    print(
        f"Largest value smaller than or equal to given sum is {solveSubsetSum(val, n, limit)}"
    )
