'''Now that you've built a general model, let's "optimize" or "fit" it to a new (preloaded) measured data set, xd, yd, by finding the specific values for model parameters a0, a1 for which the model data and the measured data line up on a plot.

This is an iterative visualization strategy, where we start with a guess for model parameters, pass them into the model(), over-plot the resulting modeled data on the measured data, and visually check that the line passes through the points. If it doesn't, we change the model parameters and try again.'''
#TASK
# Complete the function plot_data_and_model(xd, yd, ym) to over-plot the measured data yd and modeled data ym versus xd.
# Assign a guess values for parameters a0, a1, in the parameter dictionary, and use ** unpacking to pass it and xd into ym = model()
# Use plot_data_and_model() to plot xd, yd, and ym together
# Change the values of a0, a1 and repeat the previous 2 steps until the line passes through all the points.

# Complete the plotting function definition
def plot_data_with_model(xd, yd, ym):
    fig = plot_data(____, ____)  # plot measured data
    fig.axes[0].plot(____, ____, color='red')  # over-plot modeled data
    plt.show()
    return fig

# Select new model parameters a0, a1, and generate modeled `ym` from them.
a0 = ____
a1 = ____
ym = model(xd, a0, a1)

# Plot the resulting model to see whether it fits the data
fig = plot_data_with_model(xd, yd, ____)






#SOLUTION
# Complete the plotting function definition
def plot_data_with_model(xd, yd, ym):
    fig = plot_data(xd, yd)  # plot measured y data
    fig.axes[0].plot(xd, ym, color='red')  # over-plot modeled y data
    plt.show()
    return fig

# Select new model parameters a0, a1, and generate modeled `ym` from them.
a0 = 150
a1 = 25
ym = model(xd, a0, a1)

# Plot the resulting model to see whether it fits the data
fig = plot_data_with_model(xd, yd, ym)