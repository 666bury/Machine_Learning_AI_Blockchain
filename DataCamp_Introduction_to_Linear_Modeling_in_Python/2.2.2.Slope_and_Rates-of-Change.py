'''In this exercise, you will model the motion of a car driving (roughly) constant velocity by computing the average velocity over the entire trip. The linear relationship modeled is between the time elapsed and the distance traveled.

In this case, the model parameter a1, or slope, is approximated or "estimated", as the mean velocity, or put another way, the "rate-of-change" of the distance ("rise") divided by the time ("run").'''
#TASK
# Compute the the point-to-point differences of both the times and distances using numpy.diff().
# Compute an array of velocities as the ratio of the diff_distance divided by diff_times
# Compute the average and range of velocity values, using numpy methods mean, max, min.
# Plot the array of velocities to visualize the average and spread of the values.

# Compute an array of velocities as the slope between each point
diff_distances = np.diff(____)
diff_times = np.diff(____)
velocities = ____ / diff_times

# Chracterize the center and spread of the velocities
v_avg = np.____(velocities)
v_max = np.____(velocities)
v_min = np.____(velocities)
v_range = ____ - ____

# Plot the distribution of velocities
fig = plot_velocity_timeseries(times[1:], velocities)







#SOLUTION
# Compute an array of velocities as the slope between each point
diff_distances = np.diff(distances)
diff_times = np.diff(times)
velocities = diff_distances / diff_times

# Chracterize the center and spread of the velocities
v_avg = np.mean(velocities)
v_max = np.max(velocities)
v_min = np.min(velocities)
v_range = v_max - v_min

# Plot the distribution of velocities
fig = plot_velocity_timeseries(times[1:], velocities)
