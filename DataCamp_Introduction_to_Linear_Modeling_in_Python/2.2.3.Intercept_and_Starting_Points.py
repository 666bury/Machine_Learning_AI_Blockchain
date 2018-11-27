'''In this exercise, you will see the intercept and slope parameters in the context of modeling measurements taken of the volume of a solution contained in a large glass jug. The solution is composed of composed of water, grains, sugars, and yeast. The total mass of both the solution and the glass container was also recorded, but the empty container mass was not noted.

Your job is to use the preloaded pandas DataFrame df, with data columns volumes and masses to build a linear model that relates the masses (y-data) to the volumes (x-data). The slope will be an estimate of the density (change in mass / change in volume) of the solution, and the intercept will be an estimate of the empty container weight (mass when volume=0).'''
#TASK
# Import ols() from statsmodels and use it to build a model fit to the data=df with formula = "masses ~ volumes".
# Extract the slope a1 and intercept a0 with .params['Intercept'] and .params['volumes'].
# Print a0 and a1 with physically meaningful names.
# Print model_fit() and look for values matching the ones found above; look for row labels Intercept, volumes, and a column label coef.

# Import ols from statsmodels, and fit a model to the data
from statsmodels.formula.api import ols
model_fit = ols(formula="____ ~ ____", data=____).fit()

# Extract the model parameter values, and assign them to a0, a1
a0 = model_fit.params['____']
a1 = model_fit.params['____']

# Print model parameter values with meaningful names, and compare to summary()
print( "container_mass   = {:0.4f}".format(____) )
print( "solution_density = {:0.4f}".format(____) )
print( model_fit.summary() )








#SOLUTION
# Import ols from statsmodels, and fit a model to the data
from statsmodels.formula.api import ols
model_fit = ols(formula="masses ~ volumes", data=df).fit()

# Extract the model parameter values, and assign them to a0, a1
a0 = model_fit.params['Intercept']
a1 = model_fit.params['volumes']

# Print model parameter values with meaningful names, and compare to summary()
print( "container_mass   = {:0.4f}".format(a0) )
print( "solution_density = {:0.4f}".format(a1) )
print( model_fit.summary() )