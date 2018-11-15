'''There are several columns in the volunteer dataset comprised of datetimes. 
Let's take a look at the start_date_date column and extract just the month to use as a feature for modeling.'''
#TASK
# Use Pandas to_datetime() function on the volunteer["start_date_date"] column and store it in a new column called start_date_converted.
# To retrieve just the month, apply a lambda function to volunteer["start_date_converted"] that grabs the .month attribute from the row. Store this in a new column called start_date_month.
# Print the head() of just the start_date_converted and start_date_month columns.

# First, convert string column to date column
volunteer["start_date_converted"] = pd.____(____)

# Extract just the month from the converted column
volunteer["start_date_month"] = ____.apply(lambda row: ____)

# Take a look at the original and new columns
print(volunteer[[____, ____]].____)









#SOLUTION
# First, convert string column to date column
volunteer["start_date_converted"] = pd.to_datetime(volunteer["start_date_date"])

# Extract just the month from the converted column
volunteer["start_date_month"] = volunteer.apply(lambda row: row["start_date_converted"].month, axis=1)

# Take a look at the original and new columns
print(volunteer[['start_date_converted', "start_date_month"]].head())