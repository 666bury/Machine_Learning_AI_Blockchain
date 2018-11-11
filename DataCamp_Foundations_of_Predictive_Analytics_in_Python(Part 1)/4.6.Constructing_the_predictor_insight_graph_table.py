'''In the previous exercise you learned how to calculate the incidence column of the predictor insight graph table.
In this exercise, you will also add the size of the groups, and wrap everything in a function that returns the predictor insight graph table for a given variable.'''
#TASK
# Group the basetable by variable.
# Calculate the predictor insight graph table by calculating the target incidence and group sizes.
# Use the function create_pig_table to calculate the predictor insight graph table for the variable "gender".

# Function that creates predictor insight graph table
def create_pig_table(basetable, target, variable):
  
    # Create groups for each variable
    groups = basetable[[target,variable]].____(____)
    
    # Calculate size and target incidence for each group
    pig_table = groups[____].agg({'Incidence' : np.____, 'Size' : np.____}).reset_index()
    
    # Return the predictor insight graph table
    return pig_table

# Calculate the predictor insight graph table for the variable gender
pig_table_gender = ____(basetable, "target", ____)

# Print the result
print(pig_table_gender)





#SOLUTION
# Function that creates predictor insight graph table
def create_pig_table(basetable, target, variable):
  
    # Create groups for each variable
    groups = basetable[[target,variable]].groupby(variable)
    
    # Calculate size and target incidence for each group
    pig_table = groups['target'].agg({'Incidence' : np.mean, 'Size' : np.size}).reset_index()
    
    # Return the predictor insight graph table
    return pig_table

# Calculate the predictor insight graph table for the variable gender
pig_table_gender = create_pig_table(basetable, "target", "gender")

# Print the result
print(pig_table_gender)