'''In this exercise you will work with a preloaded population. You will construct a sample by drawing points at random from the population. You will compute the mean standard deviation of the sample taken from that population to test whether the sample is representative of the population. Your goal is to see where the sample statistics are the same or very close to the population statistics.'''
#TASK
# Compute and print the mean and standard deviation of the population data.
# Use the np.random.seed() method to set numpy's pseudorandom sampler seed as 42.
# Use np.random.choice() to create a sample of size=31, where size is the number of points drawn from the population.
# Compute and print the mean and standard deviation of the sample and inspect the printed values of the sample statistics and population statistics to see whether they differ.

# Compute the population statistics
print("Population mean {:.1f}, stdev {:.2f}".format( population.____(), population.____() ))

# Set random seed for reproducibility
____.____.____(42)

# Construct a sample by randomly sampling 31 points from the population
sample = np.____.____(____, size=31)

# Compare sample statistics to the population statistics
print("    Sample mean {:.1f}, stdev {:.2f}".format( sample.____(), sample.____() ))







#SOLUTION
# Compute the population statistics
print("Population mean {:.1f}, stdev {:.2f}".format( population.mean(), population.std() ))

# Set random seed for reproducibility
np.random.seed(42)

# Construct a sample by randomly sampling 31 points from the population
sample = np.random.choice(population, size=31)

# Compare sample statistics to the population statistics
print("    Sample mean {:.1f}, stdev {:.2f}".format( sample.mean(), sample.std() ))