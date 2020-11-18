import matplotlib.pyplot as plt
import numpy as np

# data to plot
student = ["Jeff", "Peter", "John", "Mary"]  # Name of the students
practice = [60, 75, 55, 80]  # Practice test scores of the students
test = [70, 90, 55, 95]  # Actual test scores of the students

n_groups = 4

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25

rects1 = plt.bar(index, practice, bar_width)

rects2 = plt.bar(index + bar_width, test, bar_width)

plt.xlabel('Students')
plt.ylabel('Scores')
plt.xticks(index + bar_width / 2, student)
plt.legend()

plt.tight_layout()
plt.show()
