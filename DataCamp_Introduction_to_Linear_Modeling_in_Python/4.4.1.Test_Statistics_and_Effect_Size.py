'''How can we explore linear relationships with bootstrap resampling? Back to the trail! For each hike plotted as one point, we can see that there is a linear relationship between total distance traveled and time elapsed. It we treat the distance traveled as an "effect" of time elapsed, then we can explore the underlying connection between linear regression and statistical inference.

In this exercise, you will separate the data into two populations, or "categories": early times and late times. Then you will look at the differences between the total distance traveled within each population. This difference will serve as a "test statistic", and it's distribution will test the effect of separating distances by times.'''
#TASK
# Use numpy "logical indexing", e.g. sample_distances[sample_times < 5], to separate the sample distances into early and late time populations.
# Use np.random.choice() with replacement=True to create a resample for each of the two time bins.
# Compute the test_statistic array as the resample_long - resample_short, and find and print the effect size and uncertainty with np.mean(), np.std().
# Plot the test_statistic distribution, using the predefined fig = plot_test_statistic().

# Create two poulations, sample_distances for early and late sample_times.
# Then resample with replacement, taking 500 random draws from each population.
group_duration_short = sample_distances[____ < 5]
group_duration_long = sample_distances[____ > 5]
resample_short = np.random.choice(____, size=500, replace=____)
resample_long = np.random.choice(____, size=500, replace=____)

# Difference the resamples to compute a test statistic distribution, then compute its mean and stdev
test_statistic = resample_long - resample_short
effect_size = np.mean(____)
standard_error = np.std(____)

# Print and plot the results
print('Test Statistic: mean={:0.2f}, stdev={:0.2f}'.format(____, ____))
fig = plot_test_statistic(____)





#SOLUTION
# Create two poulations, sample_distances for early and late sample_times.
# Then resample with replacement, taking 500 random draws from each population.
group_duration_short = sample_distances[sample_times < 5]
group_duration_long = sample_distances[sample_times > 5]
resample_short = np.random.choice(group_duration_short, size=500, replace=True)
resample_long = np.random.choice(group_duration_long, size=500, replace=True)

# Difference the resamples to compute a test statistic distribution, then compute its mean and stdev
test_statistic = resample_long - resample_short
effect_size = np.mean(test_statistic)
standard_error = np.std(test_statistic)

# Print and plot the results
print('Test Statistic: mean={:0.2f}, stdev={:0.2f}'.format(effect_size, standard_error))
fig = plot_test_statistic(test_statistic)