# Read the file 
file = open("program.c", "r")

# keep stack to keep track of the current scope
stack = []

# keep track of the current scope
for_start = False
max_for = 0
max_all = []

for line in file:
    # remove all spaces
    line = line.strip()
    line = line.replace(" ", "")

    # if for or while is found, push it to the stack
    if ("for(" in line) or ("while(" in line):
        if for_start:
            max_for += 1
        else:
            max_for = 1

        for_start = True
        if "{" in line:
            stack.append("{")

    elif for_start and "{" in line:
        stack.append("{")

    elif "}" in line and for_start:
        stack.pop()
        if len(stack) == 0:
            for_start = False

        # append max nested for and while to max_all
        if (max_for):
            max_all.append(max_for)
        max_for = 0

# print max of max_all as the max time complexity
print("Time complexity: n^" + str(max(max_all)))
