'''The forward stepwise variable selection procedure starts with an empty set of variables, and adds predictors one by one. 
In each step, the predictor that has the highest AUC in combination with the current variables is selected.

In this exercise you will learn to implement the forward stepwise variable selection procedure. 
To this end, you can use the next_best function that has been implemented for you. It can be used as follows:

next_best(current_variables,candidate_variables,target,basetable)
where current_variables is the list of variables that is already in the model and candidate_variables the list of variables that can be added next.'''
#TASK
# Use the function next_best to calculate the next best variable and assign it to next_variable.
# Update the current_variables list.
# Update the candidate_variables list.

# Find the candidate variables
candidate_variables = list(basetable.columns.values)
candidate_variables.remove("target")

# Initialize the current variables
current_variables = []

# The forward stepwise variable selection procedure
number_iterations = 5
for i in range(0, number_iterations):
    next_variable = ____(____, ____, ["target"], basetable)
    current_variables = current_variables + [____]
    candidate_variables.remove(____)
    print("Variable added in step " + str(i+1)  + " is " + next_variable + ".")
print(current_variables)






#SOLUTION
# Find the candidate variables
candidate_variables = list(basetable.columns.values)
candidate_variables.remove("target")

# Initialize the current variables
current_variables = []

# The forward stepwise variable selection procedure
number_iterations = 5
for i in range(0, number_iterations):
    next_variable = next_best(current_variables, candidate_variables, ["target"], basetable)
    current_variables = current_variables + [next_variable]
    candidate_variables.remove(next_variable)
    print("Variable added in step " + str(i+1)  + " is " + next_variable + ".")
print(current_variables)