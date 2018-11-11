'''In the previous exercise, you constructed a function that calculates the predictor insight graph table for a given variable as follows:

pig_table = create_pig_table(basetable, "target","variable")

If you want to calculate the predictor insight graph table for many variables at once, 
it is a good idea to store them in a dictionary. 
You can create a new dictionary using dictionary = {}, add elements with a key using dictionary["key"] = value and retrieve elements using the key print(dictionary["key"]).'''
#TASK
# Create an empty dictionary pig_tables.
# For each variable, create a predictor insight graph table.
# For each variable, add this predictor insight graph table to the dictionary, with as key the name of the variable.
# Print the predictor insight graph table of disc_time_since_last_gift.

# Create the list of variables for our predictor insight graph tables
variables = ["income","gender","disc_mean_gift","disc_time_since_last_gift"]

# Create an empty dictionary
pig_tables = ____

# Loop through the variables
for variable in variables:
  
    # Create a predictor insight graph table
    pig_table = ____(basetable, ____, ____)
    
    # Add the table to the dictionary
    pig_tables[____] = ____

# Print the predictor insight graph table of the variable "disc_time_since_last_gift"
print(pig_tables["____"])




#SOLUTION
# Variables you want to make predictor insight graph tables for
variables = ["income","gender","disc_mean_gift","disc_time_since_last_gift"]

# Create an empty dictionary
pig_tables = {}

# Loop through the variables
for variable in variables: 

  	# Create a predictor insight graph table
    pig_table = create_pig_table(basetable, "target",variable)

    # Add the table to the dictionary
    pig_tables[variable] = pig_table

# Print the predictor insight graph table of the variable "disc_time_since_last_gift"
print(pig_tables["disc_time_since_last_gift"])