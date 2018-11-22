'''Covariance is a measure of whether two variables change ("vary") together. It is calculated by computing the products, point-by-point, of the deviations seen in the previous exercise, dx[n]*dy[n], and then finding the average of all those products. Correlation is in essense the normalized covariance. In this exercise, you are provided with two arrays of data, which are highly correlated, and you will visualize and compute both the covariance and the correlation.'''
#TASK
# As before, compute the deviations, dx and dy, and then the normalized deviations, zx and zy.
# Compute the mean of dx*dy and assign it to covariance.
# Compute the mean of zx*zy and assign it to correlation.
# Use plot_normalized_deviations() to plot the product of zx * zy.

# Compute the covariance from the deviations.
dx = x - np.____(x)
dy = y - np.____(y)
covariance = np.____(____ * ____)
print("Covariance: ", covariance)

# Compute the correlation from the normalized deviations.
zx = dx / np.____(x)
zy = dy / np.____(y)
correlation = np.____(____ * ____)
print("Correlation: ", correlation)

# Plot the result.
fig = plot_normalized_deviations(____, ____)



#SOLUTION
# Compute the covariance from the deviations.
dx = x - np.mean(x)
dy = y - np.mean(y)
covariance = np.mean(dx * dy)
print("Covariance: ", covariance)

# Compute the correlation from the normalized deviations.
zx = dx / np.std(x)
zy = dy / np.std(y)
correlation = np.mean(zx * zy)
print("Correlation: ", correlation)

# Plot the result.
fig = plot_normalized_deviations(zx, zy)


