'''In this exercise, you will visualize the p-value, the chance that the effect (or "speed") we estimated, was the result of random variation in the sample. Your goal is to visualize this as the fraction of points in the shuffled test statistic distribution that fall to the right of the mean of the test statistic ("effect size") computed from the unshuffled samples.

To get you started, we've preloaded the group_duration_short and group_duration_long and functions compute_test_statistic(), shuffle_and_split(), and plot_test_statistic_effect()'''
#TASK
# Use compute_test_statistic() to get test_statistic_unshuffled from the group_duration_short and group_duration_long; then use np.mean() to compute effect size.
# Use shuffle_and_split() to create shuffle_half1 and shuffle_half2, and use compute_test_statistic() to compute the test_statistic_shuffled.
# Compute the p_value from test_statistic_shuffled values that are >= effect_size.
# Print the p_value and plot both test statistics using plot_test_statistic_effect().

# Compute the test stat distribution and effect size for two population groups
test_statistic_unshuffled = compute_test_statistic(____, ____)
effect_size = np.mean(____)

# Randomize the two populations, and recompute the test stat distribution
shuffled_half1, ____ = shuffle_and_split(group_duration_short, ____)
test_statistic_shuffled = compute_test_statistic(shuffled_half1, ____)

# Compute the p-value as the proportion of shuffled test stat values >= the effect size
condition = ____ >= ____
p_value = len(test_statistic_shuffled[____]) / len(test_statistic_shuffled)

# Print p-value and overplot the shuffled and unshuffled test statistic distributions
print("The p-value is = {}".format(____))
fig = plot_test_stats_and_pvalue(test_statistic_unshuffled, test_statistic_shuffled)





#SOLUTION
# Compute the test stat distribution and effect size for two population groups
test_statistic_unshuffled = compute_test_statistic(group_duration_short, group_duration_long)
effect_size = np.mean(test_statistic_unshuffled)

# Randomize the two populations, and recompute the test stat distribution
shuffled_half1, shuffled_half2 = shuffle_and_split(group_duration_short, group_duration_long)
test_statistic_shuffled = compute_test_statistic(shuffled_half1, shuffled_half2)

# Compute the p-value as the proportion of shuffled test stat values >= the effect size
condition = test_statistic_shuffled >= effect_size
p_value = len(test_statistic_shuffled[condition]) / len(test_statistic_shuffled)

# Print p-value and overplot the shuffled and unshuffled test statistic distributions
print("The p-value is = {}".format(p_value))
fig = plot_test_stats_and_pvalue(test_statistic_unshuffled, test_statistic_shuffled)