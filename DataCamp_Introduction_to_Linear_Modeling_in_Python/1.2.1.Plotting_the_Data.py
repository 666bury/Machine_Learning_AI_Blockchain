'''Everything in python is an object, even modules. Your goal in this exercise is to review the use of the object oriented interfaces to the python library matplotlib in order to visualize measured data in a more flexible and extendable work flow. The general plotting work flow looks like this:

import matplotlib.pyplot as plt 
fig, axis = plt.subplots()
axis.plot(x, y, color="green", linestyle="--", marker="s")
plt.show()'''
#TASK
# Use plt.subplots() to create figure and axis objects.
# Data have been provided in two predefined numpy arrays, times and distances.
# Use axis.plot() to plot times on the horizontal and distances on the vertical.
# Use the input key word args linestyle=" ", marker="o", and color="red" when calling axis.plot()

# Create figure and axis objects using subplots()
fig, axis = plt.____()

# Plot line using the axis.plot() method
line = axis.plot(____ , ____ , linestyle="____", marker="____", color="____")

# Use the plt.show() method to display the figure
plt.____()




#SOLUTION
# Create figure and axis objects using subplots()
fig, axis = plt.subplots()

# Plot line using the axis.plot() method
line = axis.plot(times, distances, linestyle=" ", marker="o", color="red")

# Use the plt.show() method to display the figure
plt.show()



