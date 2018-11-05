'''Once the logistic regression model is ready, it can be interesting to have a look at the coefficients to check whether the model makes sense.

Given a fitted logistic regression model logreg, you can retrieve the coefficients using the attribute coef_.
The order in which the coefficients appear, is the same as the order in which the variables were fed to the model. 
The intercept can be retrieved using the attribute intercept_.

The logistic regression model that you built in the previous exercises has been added and fitted for you in logreg.'''
#TASK
# Assign the coefficients of the logistic regression model to the list coef.
# Assign the intercept of the logistic regression model to the variable intercept.

# Construct a logistic regression model that predicts the target using age, gender_F and time_since_last gift
predictors = ["age","gender_F","time_since_last_gift"]
X = basetable[predictors]
y = basetable[["target"]]
logreg = linear_model.LogisticRegression()
logreg.fit(X, y)

# Assign the coefficients to a list coef
coef = ____.____
for p,c in zip(predictors,list(coef[0])):
    print(p + '\t' + str(c))
    
# Assign the intercept to the variable intercept
intercept = ____.____
print(intercept)




#SOLUTION
# Construct a logistic regression model that predicts the target using age, gender_F and time_since_last gift
predictors = ["age","gender_F","time_since_last_gift"]
X = basetable[predictors]
y = basetable[["target"]]
logreg = linear_model.LogisticRegression()
logreg.fit(X, y)

# Assign the coefficients to a list coef
coef = logreg.coef_
for p,c in zip(predictors,list(coef[0])):
    print(p + '\t' + str(c))
    
# Assign the intercept to the variable intercept
intercept = logreg.intercept_
print(intercept)