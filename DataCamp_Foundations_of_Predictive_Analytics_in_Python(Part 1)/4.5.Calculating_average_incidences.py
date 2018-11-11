'''The most important column in the predictor insight graph table is the target incidence column. 
This column shows the average target value for each group.'''
#TASK
# Create a dataframe basetable_income that only contains the variables target and income.
# Group this dataframe by income.
# Calculate the average target incidence for each group in income.

# Select the income and target columns
basetable_income = basetable[["____","____"]]

# Group basetable_income by income
groups = basetable_income.____("____")

# Calculate the target incidence and print the result
incidence = groups["____"].agg({"Incidence" : np.____()}).reset_index()
print(incidence)








#SOLUTION
# Select the income and target columns
basetable_income = basetable[["target","income"]]

# Group basetable_income by income
groups = basetable_income.groupby("income")

# Calculate the target incidence and print the result
incidence = groups["target"].agg({"Incidence" : np.mean}).reset_index()
print(incidence)