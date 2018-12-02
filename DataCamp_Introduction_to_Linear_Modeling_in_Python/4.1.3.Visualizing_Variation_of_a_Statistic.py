'''Previously, you have computed the variation of sample statistics. Now you'll visualize that variation.

We'll start with a preloaded population and a predefined function get_sample_statistics() to draw the samples, and return the sample statistics arrays.

Here we will use a predefined plot_hist() function that wraps the matplotlib method axis.hist(), which both bins and plots the array passed in. In this way you can see how the sample statistics have a distribution of values, not just a single value.'''
#TASK
# Pass the population into get_sample_statistics() to get the sample statistic distributions.
# Use np.linspace() to define histogram bin edges for each statistic array.
# Use the predefined plot_hist() twice, to plot the statistic distributions means and deviations as two separate histograms.

# Generate sample distribution and associated statistics
means, stdevs = get_sample_statistics(____, num_samples=100, num_pts=1000)

# Define the binning for the histograms
mean_bins = np.____(97.5, 102.5, 51)
std_bins = np.____(7.5, 12.5, 51)

# Plot the distribution of means, and the distribution of stdevs
fig = plot_hist(data=____, bins=____, data_name="Means", color='green')
fig = plot_hist(data=____, bins=____, data_name="Stdevs", color='red')









#SOLUTION
# Generate sample distribution and associated statistics
means, stdevs = get_sample_statistics(population, num_samples=100, num_pts=1000)

# Define the binning for the histograms
mean_bins = np.linspace(97.5, 102.5, 51)
std_bins = np.linspace(7.5, 12.5, 51)

# Plot the distribution of means, and the distribution of stdevs
fig = plot_hist(data=means, bins=mean_bins, data_name="Means", color='green')
fig = plot_hist(data=stdevs, bins=std_bins, data_name="Stdevs", color='red')