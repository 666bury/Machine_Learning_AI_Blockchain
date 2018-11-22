'''Building linear models is an automated way of doing something we can roughly do "manually" with data visualization and a lot of trial-and-error. The visual method is not the most efficient or precise method, but it does illustrate the concepts very well, so let's try it! Given some measured data, your goal is make guess at the slope and intercept to input into the plot, and then adjust your input until the resulting model lines up well with the data. Use the provided data xd, yd, generate modeled data with the provided function xm, ym = model(slope, intercept) and compare them using the provided plot_data_and_model(xd, yd, xm, ym).'''
#TASK
# Use the predefined function xm, ym = model(intercept, slope) to generate modeled data.
# Use the provided function fig = plot_data_and_model(x, y, xm, ym) to plot the measured data (xd, yd) and the modeled data (xm, ym) together.
# If the model does not fit the data, try different values for slope and intercept and rerun your code.
# Repeat until you believe you have the best values for slope and intercept, then submit your answer.

# Start by guessing any slope and intercept values (probably between +10 and -10)
trial_slope = ____
trial_intercept = ____

# input thoses guesses into the model function to compute the model values.
xm, ym = ____(trial_intercept, trial_slope)

# Compare your your model to the data with the plot function
fig = ____(xd, yd, xm, ym)
plt.show()

# Repeat the steps above until your slope and intercept guess makes the model line up with the data.
final_intercept = ____
final_slope = ____






#SOLUTION
# Start by guessing any slope and intercept values (probably between +10 and -10)
trial_slope = 1
trial_intercept = 2

# input thoses guesses into the model function to compute the model values.
xm, ym = model(trial_intercept, trial_slope)

# Compare your your model to the data with the plot function
fig = plot_data_and_model(xd, yd, xm, ym)
plt.show()

# Repeat the steps above until your slope and intercept guess makes the model line up with the data.
final_intercept = 2
final_slope = 1