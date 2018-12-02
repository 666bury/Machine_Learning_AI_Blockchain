'''If we create one sample of size=1000 by drawing that many points from a population. Then compute a sample statistic, such as the mean, a single value that summarizes the sample itself.

If you repeat that sampling process num_samples=100 times, you get 100 samples. Computing the sample statistic, like the mean, for each of the different samples, will result in a distribution of values of the mean. The goal then is to compute the mean of the means and standard deviation of the means.

Here you will use the preloaded population, num_samples, and num_pts, and note that the means and deviations arrays have been initialized to zero to give you containers to use for the for loop.'''
#TASK
# For each of num_samples=100, generate a sample, then compute and storing the sample statistics.
# For each iteration, create a sample by using np.random.choice() to draw 1000 random points from the population.
# For each iteration, compute and store the methods sample.mean() and sample.std() to compute the mean and standard deviation of the sample.
# For the array of means and the array of deviations, compute both the mean and standard deviation of each, and print the results.

# Initialize two arrays of zeros to be used as containers
means = np.zeros(num_samples)
stdevs = np.zeros(num_samples)

# For each iteration, compute and store the sample mean and sample stdev
for ns in range(num_samples):
    sample = np.____.choice(population, num_pts)
    means[ns] = sample.____()
    stdevs[ns] = sample.____()

# Compute and print the mean() and std() for the sample statistic distributions
print("Means:  center={:>6.2f}, spread={:>6.2f}".format(means.mean(), means.std()))
print("Stdevs: center={:>6.2f}, spread={:>6.2f}".format(stdevs.____(), stdevs.____()))










#SOLUTION
# Initialize two arrays of zeros to be used as containers
means = np.zeros(num_samples)
stdevs = np.zeros(num_samples)

# For each iteration, compute and store the sample mean and sample stdev
for ns in range(num_samples):
    sample = np.random.choice(population, num_pts)
    means[ns] = sample.mean()
    stdevs[ns] = sample.std()

# Compute and print the mean() and std() for the sample statistic distributions
print("Means:  center={:>6.2f}, spread={:>6.2f}".format(means.mean(), means.std()))
print("Stdevs: center={:>6.2f}, spread={:>6.2f}".format(stdevs.mean(), stdevs.std()))


