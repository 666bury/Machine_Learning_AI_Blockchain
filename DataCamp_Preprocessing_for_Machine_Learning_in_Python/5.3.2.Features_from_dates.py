'''Another feature engineering task to perform is month and year extraction. 
Perform this task on the date column of the ufo dataset.'''
#TASK
# Print out the head() of the date column.
# Using apply(), lambda, and the .month attribute, extract the month from the date column.
# Using apply(), lambda, and the .year attribute, extract the year from the date column.
# Take a look at the head() of the date, month, and year columns.

# Look at the first 5 rows of the date column
print(____)

# Extract the month from the date column
ufo["month"] = ufo["date"].____

# Extract the year from the date column
ufo["year"] = ufo["date"].____

# Take a look at the head of all three columns
print(____)





#SOLUTION
# Look at the first 5 rows of the date column
print(ufo['date'].head())

# Extract the month from the date column
ufo["month"] = ufo["date"].apply(lambda row: row.month)

# Extract the year from the date column
ufo["year"] = ufo["date"].apply(lambda row: row.year)

# Take a look at the head of all three columns
print(ufo[['date', 'month', 'year']].head())