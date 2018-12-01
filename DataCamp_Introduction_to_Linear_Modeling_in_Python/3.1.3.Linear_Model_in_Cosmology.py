'''Less than 100 years ago, the universe appeared to be composed of a single static galaxy, containing perhaps a million stars. Today we have observations of hundreds of billions of galaxies, each with hundreds of billions of stars, all moving.

The beginnings of the modern physical science of cosmology came with the publication in 1929 by Edwin Hubble that included use of a linear model.-http://www.pnas.org/content/15/3/168

In this exercise, you will build a model whose slope will give Hubble's Constant, which describes the velocity of galaxies as a linear function of distance from Earth.'''
#TASK
# Use the pre-loaded DataFrame with columns names, distances, and velocities
# To model a linear relationship between velocities and distances, use formula="velocities ~ distances".
# build and fit a model using ols().fit() with formula="velocities ~ distances" and data=df.
# Extract the intercept from model_fit.params and the intercept spread from model_fit.bse.

# Fit the model, based on the form of the formula
model_fit = ols(formula="velocities ~ ____", data=df).fit()

# Extract the model parameters and associated "errors" or uncertainties
a0 = model_fit.params['Intercept']
a1 = model_fit.params['____']
e0 = model_fit.bse['____']
e1 = model_fit.bse['distances']

# Print the results
print('For slope a1={:.02f}, the uncertainty in a1 is {:.02f}'.format(a1, e1))
print('For intercept a0={:.02f}, the uncertainty in a0 is {:.02f}'.format(a0, e0))






#SOLUTION
# Fit the model, based on the form of the formula
model_fit = ols(formula="velocities ~ distances", data=df).fit()

# Extract the model parameters and associated "errors" or uncertainties
a0 = model_fit.params['Intercept']
a1 = model_fit.params['distances']
e0 = model_fit.bse['Intercept']
e1 = model_fit.bse['distances']

# Print the results
print('For slope a1={:.02f}, the uncertainty in a1 is {:.02f}'.format(a1, e1))
print('For intercept a0={:.02f}, the uncertainty in a0 is {:.02f}'.format(a0, e0))