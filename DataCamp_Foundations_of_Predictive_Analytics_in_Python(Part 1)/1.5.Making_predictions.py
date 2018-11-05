'''Once your model is ready, you can use it to make predictions for a campaign. 
It is important to always use the latest information to make predictions.

In this exercise you will, given a fitted logistic regression model, learn how to make predictions for a new, updated basetable.

The logistic regression model that you built in the previous exercises has been added and fitted for you in logreg.'''
#TASK
# The latest data is in current_data. Create a data frame new_data that selects the relevant columns from current_data.
# Assign to predictions the predictions for the observations in new_data.

# Fit a logistic regression model
from sklearn import linear_model
X = basetable[["age","gender_F","time_since_last_gift"]]
y = basetable[["target"]]
logreg = linear_model.LogisticRegression()
logreg.fit(X, y)

# Create a dataframe new_data from current_data that has only the relevant predictors 
new_data = ____[[____, ____, ____]]

# Make a prediction for each observation in new_data and assign it to predictions
predictions = ____.____(____)
print(predictions[0:5])






#SOLUTION
# Fit a logistic regression model
from sklearn import linear_model
X = basetable[["age","gender_F","time_since_last_gift"]]
y = basetable[["target"]]
logreg = linear_model.LogisticRegression()
logreg.fit(X, y)

# Create a dataframe new_data from current_data that has only the relevant predictors 
new_data = current_data[["age","gender_F","time_since_last_gift"]]

# Make a prediction for each observation in new_data and assign it to predictions
predictions = logreg.predict_proba(new_data)
print(predictions[0:5])