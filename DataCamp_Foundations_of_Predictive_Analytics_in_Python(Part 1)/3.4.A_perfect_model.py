'''In this exercise you will reconstruct the lift curve of a perfect model. 
To do so, you need to construct perfect predictions.

Recall that the plot_lift_curve method requires two values for the predictions argument: the first argument for the target to be 0 and the second one for the target to be 1.'''
#TASK
# Construct a list that has perfect predictions.
# The true values of the target are in targets_test. Plot the lift curve using the perfect predictions.

# Generate perfect predictions
perfect_predictions = [(1-target , ____) for target in targets_test["target"]]

# Plot the lift curve
skplt.metrics.____(targets_test, ____)
plt.show()





#SOLUTION
# Generate perfect predictions
perfect_predictions = [(1-target, target) for target in targets_test["target"]]

# Plot the lift curve
skplt.metrics.plot_lift_curve(targets_test, perfect_predictions)
plt.show()