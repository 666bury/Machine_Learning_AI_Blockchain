'''If you take a look at the volunteer dataset types, you'll see that the column hits is type object. 
But, if you actually look at the column, you'll see that it consists of integers. 
Let's convert that column to type int.'''
#TASK
# Take a look at the .head() of the hits column.
# Use the .astype function to convert the column to type int.
# Take a look at the dtypes of the dataset again, and notice that the column type has changed.

# Print the head of the hits column
print(volunteer["hits"].____)

# Convert the hits column to type int
volunteer["hits"] = ____

# Look at the dtypes of the dataset
print(volunteer.____)



#SOLUTION
# Print the head of the hits column
print(volunteer["hits"].head())

# Convert the hits column to type int
volunteer["hits"] = volunteer["hits"].astype(int)

# Look at the dtypes of the dataset
print(volunteer.dtypes)