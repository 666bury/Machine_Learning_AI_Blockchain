'''In the previous exercises, you defined a function create_pig_table that, given a basetable and a predictor, creates a predictor insight graph table for this predictor:

pig_table = create_pig_table(basetable,target,variable)

Next, you wrote a function plot_pig that plots the predictor insight graph based on this predictor insight graph table

plot_pig(pig_table, variable)

Often, you want to make many predictor insight graphs at once. 
In this exercise, you will learn how to automatically do this using a for loop.'''
#TASK
# For each variable in variables, create a predictor insight graph table. The basetable is loaded in basetable.
# For each variable in variables, plot the predictor insight graph.

# Variables you want to make predictor insight graph tables for
variables = ["income","gender","disc_mean_gift","disc_time_since_last_gift"]

# Loop through the variables
for variable in variables: 
    
    # Create the predictor insight graph table
    pig_table = ____(____, "target", variable)
    
    # Plot the predictor insight graph
    ____(____, variable)




#SOLUTION
# Variables you want to make predictor insight graph tables for
variables = ["income","gender","disc_mean_gift","disc_time_since_last_gift"]

# Loop through the variables
for variable in variables: 
    
    # Create the predictor insight graph table
    pig_table = create_pig_table(basetable, "target", variable)
    
    # Plot the predictor insight graph
    plot_pig(pig_table, variable)