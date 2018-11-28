'''It is possible to write a numpy implementation of the analytic solution to find the minimal RSS value. But for more complex models, finding analytic formulae is not possible, and so we turn to other methods.

In this exercise you will use scipy.optimize to employ a more general approach to solve the same optimization problem.

In so doing, you will see additional return values from the method that tell answer us "how good is best". Here we will use the same measured data and parameters as seen in the last exercise for ease of comparison of the new scipy approach.'''
#TASK
# Define a function model_func(x, a0, a1) that, for a given array x returns a0 + a1*x
# Use the scipy function optimize.curve_fit() to compute optimal values for a0 and a1
# Unpack the param_opt so as to store the model parameters as a0 = param_opt[0] and a1 = param_opt[1]
# Use the predefined function compute_rss_and_plot_fit to test and verify your answer.

# Define a model function needed as input to scipy
def model_func(x, a0, a1):
    return ____ + (____*x)

# Load the measured data you want to model
x_data, y_data  = load_data()

# call curve_fit, passing in the model function and data; then unpack the results
param_opt, param_cov = optimize.curve_fit(____, x_data, y_data)
a0 = param_opt[0]  # a0 is the intercept in y = a0 + a1*x
a1 = param_opt[1]  # a1 is the slope     in y = a0 + a1*x

# test that these parameters result in a model that fits the data
fig, rss = compute_rss_and_plot_fit(____, ____)




#SOLUTION
# Define a model function needed as input to scipy
def model_func(x, a0, a1):
    return a0 + (a1*x)

# Load the measured data you want to model
x_data, y_data  = load_data()

# call curve_fit, passing in the model function and data; then unpack the results
param_opt, param_cov = optimize.curve_fit(model_func, x_data, y_data)
a0 = param_opt[0]  # a0 is the intercept in y = a0 + a1*x
a1 = param_opt[1]  # a1 is the slope     in y = a0 + a1*x

# test that these parameters result in a model that fits the data
fig, rss = compute_rss_and_plot_fit(a0, a1)