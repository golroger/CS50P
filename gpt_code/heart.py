import matplotlib.pyplot as plt

# create the x and y coordinates for the heart shape
x = [0, 0.5, 1, 0.75, 0.5, 0.25, 0, 0.25, 0.5, 0.75, 1, 0.75, 0.5, 0.25]
y = [1, 0.75, 1, 0.5, 0.25, 0, 0.25, 0.5, 0.75, 1, 0.75, 0.5, 0.25, 0]

# use matplotlib to plot the heart shape
plt.plot(x, y)
plt.show()
