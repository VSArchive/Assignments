import matplotlib.pyplot as plt

# data to plot
genre = ["Comedy", "Action", "Romance", "Drama", "SciFi"]
data = [5, 8, 2, 3, 10]

# Plot
plt.pie(data, labels=genre, autopct='%0.2f%%')

plt.axis('equal')
plt.show()
