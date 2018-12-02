'''Let's continue looking at the National Park hiking data. Notice that some distances are negative because they walked in the opposite direction from the trail head; the data are messy so let's just focus on the overall trend.

In this exercise, you goal is to use boot-strap resampling to find the distribution of speed values for a linear model, and then from that distribution, compute the best estimate for the speed and the 90th percent confidence interval of that estimate. The speed here is the slope parameter from the linear regression model to fit distance as a function of time.

To get you started, we've preloaded distance and time data, together with a pre-defined least_squares() function to compute the speed value for each resample.'''
#TASK
# Use np.random.choice() to draw sample_inds from population_inds, preserving the distance-time pairing of each datum.
# Preserve time ordering, .sort() the sample_inds, before using it to index distances and times.
# Use least_squares(distance, times) to compute linear model parameters and store a1 in resample_speeds.
# Apply np.mean() and np.percentiles() to resample_speeds, computing speed and confidence interval ci_90, and then print both.

# Resample each preloaded population, and compute speed distribution
population_inds = np.arange(0, 99, dtype=int)
for nr in range(num_resamples):
    sample_inds = np.random.choice(____, size=100, replace=True)
    sample_inds.____()
    sample_distances = distances[____]
    sample_times = times[____]
    a0, a1 = ____(sample_times, sample_distances)
    resample_speeds[nr] = ____

# Compute effect size and confidence interval, and print
speed_estimate = np.mean(____)
ci_90 = np.percentile(____, [5, 95])
print('Speed Estimate = {:0.2f}, 90% Confidence Interval: {:0.2f}, {:0.2f} '.format(____, ____[0], ____[1]))









#SOLUTION
# Resample each preloaded population, and compute speed distribution
population_inds = np.arange(0, 99, dtype=int)
for nr in range(num_resamples):
    sample_inds = np.random.choice(population_inds, size=100, replace=True)
    sample_inds.sort()
    sample_distances = distances[sample_inds]
    sample_times = times[sample_inds]
    a0, a1 = least_squares(sample_times, sample_distances)
    resample_speeds[nr] = a1

# Compute effect size and confidence interval, and print
speed_estimate = np.mean(resample_speeds)
ci_90 = np.percentile(resample_speeds, [5, 95])
print('Speed Estimate = {:0.2f}, 90% Confidence Interval: {:0.2f}, {:0.2f} '.format(speed_estimate, ci_90[0], ci_90[1]))