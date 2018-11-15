'''A good use case for taking an aggregate statistic to create a new feature is to take the mean of columns. 
Here, you have a DataFrame of running times named running_times_5k. 
For each name in the dataset, take the mean of their 5 run times.'''
#TASK
# Create a list of the columns you want to take the average of and store it in a variable named run_columns.
# Use apply to take the mean() of the list of columns and remember to set axis=1. Use lambda row: in the apply.
# Print out the DataFrame to see the mean column.

# Create a list of the columns to average
____ = ____

# Use apply to create a mean column
running_times_5k["mean"] = ____.apply(____: ____, axis=____)

# Take a look at the results
print(____)








#SOLUTION
# Create a list of the columns to average
run_columns = ["run1", "run2", "run3", "run4", "run5"]

# Use apply to create a mean column
running_times_5k["mean"] = running_times_5k.apply(lambda row: row[run_columns].mean(), axis=1)

# Take a look at the results
print(running_times_5k)