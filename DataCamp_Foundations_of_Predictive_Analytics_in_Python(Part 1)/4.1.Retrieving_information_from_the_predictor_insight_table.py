'''The predictor insight graph table contains all the information needed to construct the predictor insight graph. 
For each value the predictor takes, it has the number of observations with this value and the target incidence within this group. 
The predictor insight graph table of the predictor Country is loaded as a pandas object pig_table. 
You can access elements using indexing. 
For instance, to retrieve the target incidence of donors living in the UK, you can use:

pig_table["Incidence"][pig_table["Country"]=="UK"]'''
#TASK
# Print the number of UK donors.
# Print the target incidence of USA donors.
# Print the target incidence of India donors.

# Inspect the predictor insight graph table of Country
print(pig_table)

# Print the number of UK donors
print(pig_table["____"][pig_table["Country"]=="UK"])

# Check the target incidence of USA and India donors
print(pig_table["____"][pig_table["Country"]=="USA"])
print(____)



#SOLUTION
# Inspect the predictor insight graph table of Country
print(pig_table)

# Print the number of UK donors
print(pig_table["Size"][pig_table["Country"]=="UK"])

# Check the target incidence of USA and India donors
print(pig_table["Incidence"][pig_table["Country"]=="USA"])
print(pig_table["Incidence"][pig_table["Country"]=="India"])