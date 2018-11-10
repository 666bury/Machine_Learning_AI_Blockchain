'''The cumulative gains curve is an evaluation curve that assesses the performance of your model. 
It shows the percentage of targets reached when considering a certain percentage of your population with the highest probability to be target according to your model.

To construct this curve, you can use the .plot_cumulative_gain() method in the scikitplot module and the matplotlib.pyplot module. 
As for each model evaluation metric or curve, you need the true target values on the one hand and the predictions on the other hand to construct the cumulative gains curve.'''
#TASK
# Import the matplotlib.pyplot module.
# Import the scikitplot module.
# Construct the cumulative gains curve, given that the model outputs the values in predictions_test and the true target values are in targets_test.

# Import the matplotlib.pyplot module 
import ____.____ as plt

# Import the scikitplot module
import ____ as skplt

# Plot the cumulative gains graph
skplt.metrics.____(targets_test, ____)
plt.show()





#SOLUTION
# Import the matplotlib.pyplot module 
import matplotlib.pyplot as plt

# Import the scikitplot module
import scikitplot as skplt

# Plot the cumulative gains graph
skplt.metrics.plot_cumulative_gain(targets_test, predictions_test)
plt.show()