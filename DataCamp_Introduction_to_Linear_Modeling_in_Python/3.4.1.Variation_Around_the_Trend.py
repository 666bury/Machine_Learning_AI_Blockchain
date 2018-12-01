'''The data need not be perfectly linear, and there may be some random variation or "spread" in the measurements, and that does translate into variation of the model parameters. This variation is in the parameter is quantified by "standard error", and interpreted as "uncertainty" in the estimate of the model parameter.

In this exercise, you will use ols from statsmodels to build a model and extract the standard error for each parameter of that model.'''
#TASK
# Store the preloaded data in a DataFrame df, labeling x_data as distances and y_data as times.
# Use model_fit = ols().fit() to fit a linear model or the form formula="distances ~ times" to the data=df.
# Extract the estimated intercept model_fit.params['Intercept'] and the standard error of the slope from model_fit.bse['Intercept'].
# Repeat for the slope, and then print all 4 with meaningful names.

# Store x_data and y_data, as times and distances, in df, and use ols() to fit a model to it.
df = pd.DataFrame(dict(____=x_data, ____=y_data))
model_fit = ols(____="distances ~ times", data=____).____()

# Extact the model parameters and their uncertainties
a0 = model_fit.____['Intercept']
e0 = model_fit.____['Intercept']
a1 = model_fit.____['times']
e1 = model_fit.____['times']

# Print the results with more meaningful names
print('Estimate    of the intercept = {:0.2f}'.format(____))
print('Uncertainty of the intercept = {:0.2f}'.format(____))
print('Estimate    of the slope = {:0.2f}'.format(____))
print('Uncertainty of the slope = {:0.2f}'.format(____))





#SOLUTION
# Store x_data and y_data, as times and distances, in df, and use ols() to fit a model to it.
df = pd.DataFrame(dict(times=x_data, distances=y_data))
model_fit = ols(formula="distances ~ times", data=df).fit()

# Extact the model parameters and their uncertainties
a0 = model_fit.params['Intercept']
e0 = model_fit.bse['Intercept']
a1 = model_fit.params['times']
e1 = model_fit.bse['times']

# Print the results with more meaningful names
print('Estimate    of the intercept = {:0.2f}'.format(a0))
print('Uncertainty of the intercept = {:0.2f}'.format(e0))
print('Estimate    of the slope = {:0.2f}'.format(a1))
print('Uncertainty of the slope = {:0.2f}'.format(e1))