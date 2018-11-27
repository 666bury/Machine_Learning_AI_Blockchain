'''Previously, you have been given a pre-defined model to work with. In this exercise, you will implement a model function that returns model values for y, computed from input x data, and any input coefficients for the "zero-th" order term a0, the "first-order" term a1, and a quadratic term a2 of a model. Recall that "first order" is linear, so we'll set the defaults for this general linear model with a2=0, but later, we will change this for comparison.'''
#TASK
# Complete the function definition model() so it takes x, and default inputs a0=3, a1=2, a2=0 as input, and returns y.
# Create an array of values x using the numpy method np.linspace().
# Pass x into your model() without specifying a0, a1, a2, to get default predicted y values.
# Use the pre-defined plot_prediction() to see a plot of the resulting data x and y.

# Define the general model as a function
def model(x, a0=____, a1=____, a2=____):
    return a0 + (a1*____) + (a2*____*____)

# Generate array x, then predict ym values for specific, non-default a0 and a1
x = np.____(-10, 10, 21)
ym = model(____)

# Plot the results, ym versus x
fig = plot_prediction(____, ____)







#SOLUTION
# Define the general model as a function
def model(x, a0=3, a1=2, a2=0):
    return a0 + (a1*x) + (a2*x*x)

# Generate array x, then predict ym values for specific, non-default a0 and a1
x = np.linspace(-10, 10, 21)
ym = model(x, a0=3, a1=2, a2=0)

# Plot the results, ym versus x
fig = plot_prediction(x, ym)