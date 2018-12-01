'''In this exercise you'll compute another measure of goodness, R-squared. R-squared is the ratio of the variance of the residuals divided by the variance of the data we are modeling, and in so doing, is a measure of how much of the variance in your data is "explained" by your model, as expressed in the spread of the residuals.

Here we have pre-loaded the data x_data,y_data and the model predictions y_model for the best fit model; you're goal is to compute the R-squared measure to quantify how much this linear model accounts for variation in the data.'''
#TASK
# Compute the residuals, by subtracting the y_data from the y_model, and the deviations, by subtracting the y_data from the np.mean() of the y_data.
# Compute the variance of the residuals and the variance of the deviations, using np.mean() and np.square() to each.
# Compute the r_squared as 1 minus the ratio var_residuals / var_deviations, and print the result

# Compute the residuals and the deviations
residuals = ____ - y_data
deviations = np.____(____) - y_data

# Compute the variance of the residuals and deviations
var_residuals = np.____(np.____(____))
var_deviations = np.____(np.____(____))

# Compute r_squared as 1 - the ratio of RSS/Variance
r_squared = 1 - (____ / ____)
print('R-squared is {:0.2f}'.format(____))





#SOLUTION
# Compute the residuals and the deviations
residuals = y_data - y_model
deviations = np.mean(y_data) - y_data

# Compute the variance of the residuals and deviations
var_residuals = np.mean(np.square(residuals))
var_deviations = np.mean(np.square(deviations))

# Compute r_squared as 1 - the ratio of RSS/Variance
r_squared = 1 - (var_residuals / var_residuals)
print('R-squared is {:0.2f}'.format(r_squared))