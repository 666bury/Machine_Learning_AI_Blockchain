'''One common use of modeling is interpolation to determine a value "inside" or "in between" the measured data points. 
In this exercise, you will make a prediction for the value of the dependent variable distances for a given independent variable times that falls "in between" two measurements from a road trip, 
where the distances are those traveled for the given elapse times.'''
#TASK
# Inspect the predefined data arrays, times and distances, and the preloaded plot.
# Based on your rough inspection, estimate the distance_traveled away from the starting position as of elapse_time = 2.5 hours.
# Assign your answer to distance_traveled.

# Compute the total change in distance and change in time
total_distance = ____[-1] - ____[0]
total_time = ____[-1] - ____[0]

# Estimate the slope of the data from the ratio of the changes
average_speed = total_distance / total_time

# Predict the distance traveled for a time not measured
elapse_time = 2.5
distance_traveled = average_speed * elapse_time
print("The distance traveled is {}".format(distance_traveled))





#SOLUTION
# Compute the total change in distance and change in time
total_distance = distances[-1] - distances[0]
total_time = times[-1] - times[0]

# Estimate the slope of the data from the ratio of the changes
average_speed = total_distance / total_time

# Predict the distance traveled for a time not measured
elapse_time = 2.5
distance_traveled = average_speed * elapse_time
print("The distance traveled is {}".format(distance_traveled))





