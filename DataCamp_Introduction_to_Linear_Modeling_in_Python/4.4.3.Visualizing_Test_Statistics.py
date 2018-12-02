'''In this exercise, you will approach the null hypothesis by comparing the distribution of a test statistic arrived at from two different ways.

First, you will examine two "populations", grouped by early and late times, and computing the test statistic distribution. Second, shuffle the two populations, so the data is no longer time ordered, and each has a mix of early and late times, and then recompute the test statistic distribution.

To get you started, we've pre-loaded the two time duration groups, group_duration_short and group_duration_long, and two functions, shuffle_and_split() and plot_test_statistic().'''
#TASK
# Use np.random.choice() to resample group_duration_short and group_duration_long, and difference the resamples to compute the test_statistic_unshuffled.
# Use shuffle_and_split() to shuffle the two populations, and then splitting into two new shuffled populations.
# Resample the shuffled populations, and difference the results to compute a new test_statistic_shuffled.
# Use plot_test_statistic() to plot both test statistic distributions, and compare visually.

# From the unshuffled groups, compute the test statistic distribution
resample_short = np.random.choice(____, size=500, replace=____)
resample_long = np.random.choice(____, size=500, replace=____)
test_statistic_unshuffled = ____ - ____

# Shuffle two populations, cut in half, and recompute the test statistic
shuffled_half1, shuffled_half2 = shuffle_and_split(____, ____)
resample_half1 = np.random.choice(____, size=500, replace=____)
resample_half2 = np.random.choice(____, size=500, replace=____)
test_statistic_shuffled = resample_half2 - resample_half1

# Plot both the unshuffled and shuffled results and compare
fig = plot_test_statistic(____, label='Unshuffled')
fig = plot_test_statistic(____, label='Shuffled')









#SOLUTION
# From the unshuffled populations, compute the test statistic distribution
resample_short = np.random.choice(group_duration_short, size=500, replace=True)
resample_long = np.random.choice(group_duration_long, size=500, replace=True)
test_statistic_unshuffled = resample_long - resample_short

# Shuffle two populations, cut in half, and recompute the test statistic
shuffled_half1, shuffled_half2 = shuffle_and_split(group_duration_short, group_duration_long)
resample_half1 = np.random.choice(shuffled_half1, size=500, replace=True)
resample_half2 = np.random.choice(shuffled_half2, size=500, replace=True)
test_statistic_shuffled = resample_half2 - resample_half1

# Plot both the unshuffled and shuffled results and compare
fig = plot_test_statistic(test_statistic_unshuffled, label='Unshuffled')
fig = plot_test_statistic(test_statistic_shuffled, label='Shuffled')
