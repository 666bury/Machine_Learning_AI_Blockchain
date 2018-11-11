'''Instead of discretizing the continuous variables one by one, it is easier to discretize them automatically.
 To get a list of all the columns in Python, you can use

variables  = basetable.columns

Only variables that are continuous should be discretized. 
You can verify whether variables should be discretized by checking whether they have more than a predefined number of different values.'''
#TASK
# Make a list variables containing all the column names of the basetable.
# Create a loop that checks all the variables in the list variables.
# Complete the ifstatement such that only variables with more than 5 different values are discretized.
# Group the continuous variables in 10 bins using the qcut method.


# Print the columns in the original basetable
print(basetable.columns)

# Get all the variable names except "target"
variables = list(____.____)
variables.remove("target")

# Loop through all the variables and discretize in 10 bins if there are more than 5 different values
for variable in ____:
    if len(basetable.groupby(____))>____:
        new_variable = "disc_" + variable
        basetable[new_variable] = pd.qcut(basetable[____], ____)
        
# Print the columns in the new basetable
print(basetable.columns)





#SOLUTION
# Print the columns in the original basetable
print(basetable.columns)

# Get all the variable names except "target"
variables = list(basetable.columns)
variables.remove("target")

# Loop through all the variables and discretize in 10 bins if there are more than 5 different values
for variable in variables:
    if len(basetable.groupby(variable))>5:
        new_variable = "disc_" + variable
        basetable[new_variable] = pd.qcut(basetable[variable], 10)
        
# Print the columns in the new basetable
print(basetable.columns)