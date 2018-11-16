'''Now that you've identified redundant columns in the volunteer dataset, 
let's perform feature selection on the dataset to return a DataFrame of the relevant features.'''
#TASK
# Create a list of redundant column names and store it in the to_drop variable, in alphabetical order. You'll see three related features: locality, region, and postalcode. For now, let's only keep postalcode.
# Drop the columns from the dataset using drop().
# Print out the head() of the DataFrame to see the selected columns.

# Create a list of redundant column names to drop
to_drop = ["____", "____", "____", "____", "____"]

# Drop those columns from the dataset
volunteer_subset = ____.____(____, ____)

# Print out the head of the new dataset
print(____)




#SOLUTION
# Create a list of redundant column names to drop
to_drop = ["category_desc", "created_date", "locality", "region", "vol_requests"]

# Drop those columns from the dataset
volunteer_subset = volunteer.drop(to_drop, axis=1)

# Print out the head of the new dataset
print(volunteer_subset.head())