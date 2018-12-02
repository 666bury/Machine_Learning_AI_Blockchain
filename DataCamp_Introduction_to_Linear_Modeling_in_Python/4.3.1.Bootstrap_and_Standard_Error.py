'''Imagine a National Park where park rangers hike each day as part of maintaining the park trails. They don't always take the same path, but they do record their final distance and time. We'd like to build a statistical model of the variations in daily distance traveled from a limited sample of data from one ranger.

Your goal is to use bootstrap resampling, computing one mean for each resample, to create a distribution of means, and then compute standard error as a way to quantify the "uncertainty" in the sample statistic as an estimator for the population statistic.

Use the preloaded sample_data array of 500 independent measurements of distance traveled. For now, we this is a simulated data set to simplify this lesson. Later, we'll see more realistic data.'''
#TASK
# Assign the sample_data as the model for the population.
# Iterate num_resamples times, using np.random.choice() each time to generate a bootstrap_sample of size=resample_size taken from the population_model, with replacement=True, and compute and store the sample mean each time.
# Compute and print the np.mean() and np.std() of bootstrap_means.
# Use the predefined plot_data_hist() and visualize the bootstrap_means distribution.

# Use the sample_data as a model for the population
population_model = ____

# Resample the population_model 100 times, computing the mean each sample
for nr in range(num_resamples):
    bootstrap_sample = np.random.____(population_model, size=____, replace=____)
    bootstrap_means[nr] = np.____(bootstrap_sample)

# Compute and print the mean, stdev of the resample distribution of means
distribution_mean = np.mean(____)
standard_error = np.std(____)
print('Bootstrap Distribution: center={:0.1f}, spread={:0.1f}'.format(____, ____))

# Plot the bootstrap resample distribution of means
fig = plot_data_hist(____)








#SOLUTION
# Use the sample_data as a model for the population
population_model = sample_data

# Resample the population_model 100 times, computing the mean each sample
for nr in range(num_resamples):
    bootstrap_sample = np.random.choice(population_model, size=resample_size, replace=True)
    bootstrap_means[nr] = np.mean(bootstrap_sample)

# Compute and print the mean, stdev of the resample distribution of means
distribution_mean = np.mean(bootstrap_means)
standard_error = np.std(bootstrap_means)
print('Bootstrap Distribution: center={:0.1f}, spread={:0.1f}'.format(distribution_mean, standard_error))

# Plot the bootstrap resample distribution of means
fig = plot_data_hist(bootstrap_means)