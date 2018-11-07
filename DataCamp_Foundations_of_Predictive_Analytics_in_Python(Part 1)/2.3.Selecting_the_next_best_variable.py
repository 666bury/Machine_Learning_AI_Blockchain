'''The forward stepwise variable selection method starts with an empty variable set and proceeds in steps, where in each step the next best variable is added. 
To implement this procedure, two handy functions have been implemented for you.

The auc function calculates for a given variable set variables the AUC of the model that uses this variable set as predictors. 
The next_best function calculates which variable should be added in the next step to the variable list.

In this exercise, you will experiment with these functions to better understand their purpose. 
You will calculate the AUC of a given variable set, calculate which variable should be added next, and verify that this indeed results in an optimal AUC.'''
#TASK
# The auc function has been implemented for you. Calculate the AUC of a model that uses "max_gift", "mean_gift" and "min_gift" as predictors. You should pass these variables in a list as the first argument to the auc function.
# The next_best function has been implemented for you. Calculate which variable should be added next, given that "max_gift", "mean_gift" and "min_gift" are currently in the model, and "age" and "gender_F" are the candidate next predictors. The first argument of the next_best function is a list with the current variables, while the second argument is a list with the candidate predictors.
# Calculate the AUC of a model that uses "max_gift", "mean_gift", "min_gift" and "age" as predictors.
# Calculate the AUC of a model that uses "max_gift", "mean_gift", "min_gift" and "gender_F" as predictors.

# Calculate the AUC of a model that uses "max_gift", "mean_gift" and "min_gift" as predictors
auc_current = ____([____, ____, ____], ["target"], basetable)
print(round(auc_current,4))

# Calculate which variable among "age" and "gender_F" should be added to the variables "max_gift", "mean_gift" and "min_gift"
next_variable = ____([____, ____, ____], [____, ____], ["target"], basetable)
print(next_variable)

# Calculate the AUC of a model that uses "max_gift", "mean_gift", "min_gift" and "age" as predictors
auc_current_age = ____([____, ____, ____, ____], ["target"], basetable)
print(round(auc_current_age,4))

# Calculate the AUC of a model that uses "max_gift", "mean_gift", "min_gift" and "gender_F" as predictors
auc_current_gender_F = ____([____], ["target"], basetable)
print(round(auc_current_gender_F,4))





#SOLUTION
# Calculate the AUC of a model that uses "max_gift", "mean_gift" and "min_gift" as predictors
auc_current = auc(['max_gift', "mean_gift", "min_gift"], ["target"], basetable)
print(round(auc_current,4))

# Calculate which variable among "age" and "gender_F" should be added to the variables "max_gift", "mean_gift" and "min_gift"
next_variable = next_best(["max_gift", "mean_gift", "min_gift"], ["age", "gender_F"], ["target"], basetable)
print(next_variable)

# Calculate the AUC of a model that uses "max_gift", "mean_gift", "min_gift" and "age" as predictors
auc_current_age = auc(["max_gift", "mean_gift", "min_gift", "age"], ["target"], basetable)
print(round(auc_current_age,4))

# Calculate the AUC of a model that uses "max_gift", "mean_gift", "min_gift" and "gender_F" as predictors
auc_current_gender_F = auc(["max_gift", "mean_gift", "min_gift", "gender_F"], ["target"], basetable)
print(round(auc_current_gender_F,4))