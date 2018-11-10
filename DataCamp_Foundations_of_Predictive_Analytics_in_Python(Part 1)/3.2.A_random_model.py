'''In this exercise you will reconstruct the cumulative gains curve's baseline, that is, the cumulative gains curve of a random model.

To do so, you need to construct random predictions. 
The plot_cumulative_gain method requires two values for these predictions: one for the target to be 0 and one for the target to be 1. 
These values should sum to one, so a valid list of predictions could for instance be [(0.02,0.98),(0.27,0.73),...,(0.09,0.91)].

In Python, you can generate a random value between values a and b as follows:

import random
random_value = random.uniform(a,b)'''
#TASK
# Import the random, matplotlib and scikitplot modules
# Construct a list random_predictions that contains random numbers between 0 and 1.
# Adjust the list random_predictions such that it contains tuples (r,a) with r the original value of the list and a such that r+a=1.
# The true values of the target are in targets_test. Show the cumulative gains graph of your random model.

# Import the modules
import ____
import ____ as plt
import ____ as skplt

# Generate random predictions
random_predictions = [random.uniform(____,____) for _ in range(len(targets_test))]

# Adjust random predictions
random_predictions = [(r, ____ - ____) for r in random_predictions]

# Plot the cumulative gains graph
skplt.metrics.plot_cumulative_gain(targets_test, ____)
plt.show()




#SOLUTION
# Import the modules
import random
import matplotlib.pyplot as plt
import scikitplot as skplt

# Generate random predictions
random_predictions = [random.uniform(0,1) for _ in range(len(targets_test))]

# Adjust random_predictions
random_predictions = [(r,1-r) for r in random_predictions]

# Plot the cumulative gains graph
skplt.metrics.plot_cumulative_gain(targets_test, random_predictions)
plt.show()
