'''One of the columns in the volunteer dataset, category_desc, gives category descriptions for the volunteer opportunities listed. 
Because it is a categorical variable with more than two categories, we need to use one-hot encoding to transform this column numerically. 
Use Pandas' get_dummies() function to do so.'''
#TASK
# Call get_dummies() on the volunteer["category_desc"] column to create the encoded columns and assign it to category_enc.
# Print out the head() of the category_enc variable to take a look at the encoded columns.

# Transform the category_desc column
category_enc = pd.____(____)

# Take a look at the encoded columns
print(____)







#SOLUTION
# Transform the category_desc column
category_enc = pd.get_dummies(volunteer["category_desc"])

# Take a look at the encoded columns
print(category_enc.head())