'''The formulae below are the result of working through the calculus discussed in the introduction. In this exercise, we'll trust that the calculus correct, and implement these formulae in code using numpy.

a1=covariance(x,y)variance(x)
a0=mean(y)−a1mean(x)'''
#TASK
# Compute the means and deviations of the two variables x, y from the preloaded data.
# Use np.sum() to complete the least-squares formulae, and use them to compute the optimal values for a0 and a1.
# Use model() to build the model values y_model from those optimal slope a1 and intercept a0 values`.
# Use the pre-defined compute_rss_and_plot_fit() to visually confirm that this optimal model fits the data.

# prepare the means and deviations of the two variables
x_mean = np.____(x)/len(x)
y_mean = np.____(y)/len(y)
x_dev = x - ____
y_dev = y - ____

# Complete least-squares formulae to find the optimal a0, a1
a1 = np.sum(____ * ____) / np.sum( np.square(____) )
a0 = ____ - (a1 * ____)

# Use the those optimal model parameters a0, a1 to build a model
y_model = model(x, ____, ____)

# plot to verify that the resulting y_model best fits the data y
fig, rss = compute_rss_and_plot_fit(a0, a1)





#SOLUTION
# prepare the means and deviations of the two variables
x_mean = np.sum(x)/len(x)
y_mean = np.sum(y)/len(y)
x_dev = x - x_mean
y_dev = y - y_mean

# Complete least-squares formulae to find the optimal a0, a1
a1 = np.sum(x_dev * y_dev) / np.sum( np.square(x_dev) )
a0 = y_mean - (a1 * x_mean)

# Use the those optimal model parameters a0, a1 to build a model
y_model = model(x, a0, a1)

# plot to verify that the resulting y_model best fits the data y
fig, rss = compute_rss_and_plot_fit(a0, a1)