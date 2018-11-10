'''The cumulative gains graph can be used to estimate how many donors one should address to make a certain profit. 
Indeed, the cumulative gains graph shows which percentage of all targets is reached when addressing a certain percentage of the population. 
If one knows the reward of a campaign, it follows easily how many donors should be targeted to reach a certain profit.

In this exercise, you will calculate how many donors you should address to obtain a 30 000 Euro profit.'''
#TASK
# Plot the cumulative gains curve. The predictions are in predictions_test and the true target values are in targets_test.
# Assume the cost of a campaign is 0 Euro and the reward of addressing a target is 50 Euro. Fill out how many targets should be reached to make 30 000 Euro profit.
# There are 1000 targets in total. Fill out which percentage of the targets should be addressed.
# Use the cumulative gains curve to know which percentage of the population should be addressed. Round to the tenth.
# Given that the population consists of 10 000 donors, fill out how many donors should be addressed.

# Plot the cumulative gains
skplt.metrics.plot_cumulative_gain(____, ____)
plt.show()

# Number of targets you want to reach
number_targets_toreach = ____ / ____
perc_targets_toreach = ____ / ____
cumulative_gains = ____
number_donors_toreach = ____ * ____



#SOLUTION
# Plot the cumulative gains
skplt.metrics.plot_cumulative_gain(targets_test, predictions_test)
plt.show()

# Number of targets you want to reach
number_targets_toreach = 30000 / 50
perc_targets_toreach = number_targets_toreach / 1000
cumulative_gains = 0.4
number_donors_toreach = cumulative_gains * 10000