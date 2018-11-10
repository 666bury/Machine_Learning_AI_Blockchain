'''The lift curve is an evaluation curve that assesses the performance of your model. 
It shows how many times more than average the model reaches targets.

To construct this curve, you can use the plot_lift_curve method in the scikitplot module and the matplotlib.pyplot module. 
As for each model evaluation metric or curve, you need the true target values on the one hand and the predictions on the other hand to construct the cumulative gains curve.'''
#TASK
# Import the matplotlib.pyplot module.
# Import the scikitplot module.
# Construct the cumulative gains curve, given that the model outputs the values in predictions_test and the true target values are in targets_test.

#=-0 Import the matplotlib.pyplot module 
____ as plt

# Import the scikitplot module
____ as skplt

# Plot the lift curve
skplt.metrics.____(____, ____)
plt.show()





#SOLUTION
# Import the matplotlib.pyplot module 
import matplotlib.pyplot as plt

# Import the scikitplot module
import scikitplot as skplt

# Plot the lift curve
skplt.metrics.plot_lift_curve(targets_test, predictions_test)
plt.show()