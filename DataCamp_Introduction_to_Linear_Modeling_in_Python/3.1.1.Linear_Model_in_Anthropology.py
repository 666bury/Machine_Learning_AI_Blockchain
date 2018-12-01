'''If you found part of a skeleton, from an adult human that lived thousands of years ago, how could you estimate the height of the person that it came from? This exercise is in part inspired by the work of forensic anthropologist Mildred Trotter, who built a regression model for the calculation of stature estimates from human "long bones" or femurs that is commonly used today.

In this exercise, you'll use data from many living people, and the python library scikit-learn, to build a linear model relating the length of the femur (thigh bone) to the "stature" (overall height) of the person. Then, you'll apply your model to make a prediction about the height of your ancient ancestor.'''
#TASK
# import LinearRegression from sklearn.linear_model and initialize the model with fit_intercept=False
# Reshape the pre-loaded data arrays legs and heights, from "1-by-N" to "N-by-1" arrays.
# Pass the reshaped arrays legs and heights into model.fit().
# use model.predict() to predict the value fossil_height for the newly found fossil fossil_leg = 50.7.

# import the sklearn class LinearRegression and initialize the model
from sklearn.____ import ____
model = LinearRegression(fit_intercept=False)

# Prepare the measured data arrays and fit the model to them
legs = legs.reshape(len(____),1)
heights = heights.reshape(len(____),1)
model.fit(____, heights)

# Use the fitted model to make a prediction for the found femur
fossil_leg = 50.7
fossil_height = model.predict(____)
print("Predicted fossil height = {:0.2f} cm".format(fossil_height[0,0]))







#SOLUTION
# import the sklearn class LinearRegression and initialize the model
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=False)

# Prepare the measured data arrays and fit the model to them
legs = legs.reshape(len(legs),1)
heights = heights.reshape(len(heights),1)
model.fit(legs, heights)

# Use the fitted model to make a prediction for the found femur
fossil_leg = 50.7
fossil_height = model.predict(fossil_leg)
print("Predicted fossil height = {:0.2f} cm".format(fossil_height[0,0]))