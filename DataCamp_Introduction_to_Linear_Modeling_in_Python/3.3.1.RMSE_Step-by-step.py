'''In this exercise, you will quantify the over-all model "goodness-of-fit" of a pre-built model, by computing one of the most common quantitative measures of model quality, the RMSE, step-by-step.

Start with the pre-loaded data x_data and y_data, and use it with a predefined modeling function model_fit_and_predict().'''
#TASK
# Compute y_model values from model_fit_and_predict(x_data, y_data)
# Compute the residuals as the difference between y_model and y_data
# Use np.sum() and np.square() to compute RSS, and divide by len(residuals) to get MSE
# Take the np.sqrt() of MSE to get RMSE, and print all results.

# Build the model and compute the residuals "model - data"
y_model = model_fit_and_predict(x_data, y_data)
residuals = ____ - ____

# Compute the RSS, MSE, and RMSE and print the results
RSS = np.____(np.____(residuals))
MSE = ____/len(residuals)
RMSE = np.____(____)
print('RMSE = {:0.2f}, MSE = {:0.2f}, RSS = {:0.2f}'.format(RMSE, MSE, RSS))






#SOLUTION
# Build the model and compute the residuals "model - data"
y_model = model_fit_and_predict(x_data, y_data)
residuals = y_model - y_data

# Compute the RSS, MSE, and RMSE and print the results
RSS = np.sum(np.square(residuals))
MSE = RSS/len(residuals)
RMSE = np.sqrt(MSE)
print('RMSE = {:0.2f}, MSE = {:0.2f}, RSS = {:0.2f}'.format(RMSE, MSE, RSS))