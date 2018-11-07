'''Adding more variables and therefore more complexity to your logistic regression model does not automatically result in more accurate models. 
In this exercise you can verify whether adding 3 variables to a model leads to a more accurate model.

variables_1 and variables_2 are available in your environment: you can print them to the console to explore what they look like.'''
#TASK
# Fit the logreg model using variables_2 which contains 3 additional variables compared to variables_1.
# Make predictions for this model.
# Calculate the AUC of this model.

# Create appropriate dataframes
X_1 = basetable[variables_1]
X_2 = basetable[variables_2]
y = basetable[["target"]]

# Create the logistic regression model
logreg = linear_model.LogisticRegression()

# Make predictions using the first set of variables and assign the AUC to auc_1
logreg.fit(X_1, y)
predictions_1 = logreg.predict_proba(X_1)[:,1]
auc_1 = roc_auc_score(y, predictions_1)

# Make predictions using the second set of variables and assign the AUC to auc_2
logreg.____(____, ____)
predictions_2 = ____.____(____)[____,____]
auc_2 = ____(____, ____)

# Print auc_1 and auc_2
print(round(auc_1,2))
print(round(auc_2,2))




#SOLUTION
# Consider two sets of variables
variables_1 = ["mean_gift","income_low"]
variables_2 = ["mean_gift","income_low","gender_F","country_India","age"]

# Create appropriate dataframes
X_1 = basetable[variables_1]
X_2 = basetable[variables_2]
y = basetable[["target"]]

# Create the logistic regression model
logreg = linear_model.LogisticRegression()

# Make predictions using the first set of variables and assign the AUC to auc_1
logreg.fit(X_1, y)
predictions_1 = logreg.predict_proba(X_1)[:,1]
auc_1 = roc_auc_score(y, predictions_1)

# Make predictions using the second set of variables and assign the AUC to auc_2
logreg.fit(X_2, y)
predictions_2 = logreg.predict_proba(X_2)[:,1]
auc_2 = roc_auc_score(y, predictions_2)

# Print auc_1 and auc_2
print(round(auc_1,2))
print(round(auc_2,2))