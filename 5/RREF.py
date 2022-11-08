import random

M = [[random.randint(0, 1) for i in range(4)] for j in range(4)]

M = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1],
]

for i in M:
    print(i)

print("\n")

for l in M:
    # For i in Rows in reverse order
    for i in range(len(M)-1, 0, -1):
        # for j in Columns
        for j in range(i):
            stop = False
            k = 0
            # try substracting from current row with all previous rows
            while not stop:
                if M[i][j] != 0:
                    R = [M[i][x]-M[k][x] for x in range(len(M[i]))]
                    # if all in row before current element are 0 then save
                    if all(v == 0 for v in R[0:j]):
                        M[i] = R

                # if substraction with current row not result in 0 then try with next row
                if M[i][j] != 0:
                    k += 1
                    if k == i:
                        stop = True
                else:
                    stop = True

for i in M:
    print(i)
