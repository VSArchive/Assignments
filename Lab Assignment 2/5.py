d = {1: ['a', 'b'], 2: ['c', 'd']}

# d = {}
# a = []
#
# x = 0
#
# while x != -1:
#     x = int(input("Enter Key : "))
#     if x != -1:
#         y = input("Enter Value 1 : ")
#         z = input("Enter Value 2 : ")
#         a.append(y)
#         d.update({x: [y, z]})

for i in d:
    if len(d) > i:
        print(d[i][0] + d[i + 1][0])
        print(d[i][0] + d[i + 1][1])
        print(d[i][1] + d[i + 1][0])
        print(d[i][1] + d[i + 1][1])
