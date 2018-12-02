'''In this exercise, we formulate the null hypothesis as

short and long time durations have no effect on total distance traveled.

We interpret the "zero effect size" to mean that if we shuffled samples between short and long times, so that two new samples each have a mix of short and long duration trips, and then compute the test statistic, on average it will be zero.

In this exercise, your goal is to perform the shuffling and resampling. Start with the predefined group_duration_short and group_duration_long which are the un-shuffled time duration groups.'''
#TASK
# Use np.concatenate() to combine the two populations, and then use np.random.shuffle() to shuffle the values inside that container.
# Slice the shuffle_bucket in half and use np.random.choice() to resample each shuffle_half.
# Compute the test_statistic as a difference of the resampled arrays
# Compute the effect_size as the np.mean() of the test_statistic, and print the result.

# Shuffle the time-ordered distances, then slice the result into two populations.
shuffle_bucket = np.____((group_duration_short, group_duration_long))
np.random.shuffle(____)
slice_index = len(shuffle_bucket)//2
shuffled_half1 = shuffle_bucket[0:____]
shuffled_half2 = shuffle_bucket[____+1:]

# Create new samples from each shuffled population, and compute the test statistic
resample_half1 = np.random.choice(____, size=500, replace=____)
resample_half2 = np.random.choice(____, size=500, replace=____)
test_statistic = ____ - ____

# Compute and print the effect size
effect_size = np.mean(____)
print('Test Statistic, after shuffling, mean = {}'.format(____))






#SOLUTION
# Shuffle the time-ordered distances, then slice the result into two populations.
shuffle_bucket = np.concatenate((group_duration_short, group_duration_long))
np.random.shuffle(shuffle_bucket)
slice_index = len(shuffle_bucket)//2
shuffled_half1 = shuffle_bucket[0:slice_index]
shuffled_half2 = shuffle_bucket[slice_index+1:]

# Create new samples from each shuffled population, and compute the test statistic
resample_half1 = np.random.choice(shuffled_half1, size=500, replace=True)
resample_half2 = np.random.choice(shuffled_half2, size=500, replace=True)
test_statistic = resample_half2 - resample_half1

# Compute and print the effect size
effect_size = np.mean(test_statistic)
print('Test Statistic, after shuffling, mean = {}'.format(effect_size))