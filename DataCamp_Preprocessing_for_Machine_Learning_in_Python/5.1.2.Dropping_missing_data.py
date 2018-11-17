'''Let's remove some of the rows where certain columns have missing values. 
We're going to look at the length_of_time column, the state column, and the type column. 
If any of the values in these columns are missing, we're going to drop the rows.'''
#TASK
# Check how many values are missing in the length_of_time, state, and type columns, using isnull() to check for nulls and sum() to calculate how many exist.
# Use boolean indexing to filter out the rows with those missing values, using notnull() to check the column. Here, we can chain together each column we want to check.
# Print out the shape of the new ufo_no_missing dataset.

# Check how many values are missing in the length_of_time, state, and type columns
print(ufo[[____, ____, ___]].____.____)

# Keep only rows where length_of_time, state, and type are not null
ufo_no_missing = ufo[____ & 
          ____ & 
          ____]

# Print out the shape of the new dataset
____







#SOLUTION
# Check how many values are missing in the length_of_time, state, and type columns
print(ufo[['length_of_time', 'state', 'type']].isnull().sum())

# Keep only rows where length_of_time, state, and type are not null
ufo_no_missing = ufo[ufo['length_of_time'].notnull() & 
          ufo['state'].notnull() & 
          ufo['type'].notnull()]

# Print out the shape of the new dataset
print(ufo_no_missing.shape)

