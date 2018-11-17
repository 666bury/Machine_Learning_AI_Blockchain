'''In this section, you'll investigate the variance of columns in the UFO dataset to determine which features should be standardized. 
After taking a look at the variances of the seconds and minutes column, you'll see that the variance of the seconds column is extremely high. 
Because seconds and minutes are related to each other (an issue we'll deal with when we select features for modeling), let's log normlize the seconds column.'''
#TASK
# Use the var() method on the seconds and minutes columns to check the variance. Notice how high the variance is on the seconds column.
# Using np.log() perform log normalization on the seconds column, transforming it into a new column named seconds_log.
# Print out the variance of the seconds_log column.

# Check the variance of the seconds and minutes columns
print(____)

# Log normalize the seconds column
ufo["seconds_log"] = ____

# Print out the variance of just the seconds_log column
print(____)








#SOLUTION
# Check the variance of the seconds and minutes columns
print(ufo[['seconds','minutes']].var())

# Log normalize the seconds column
ufo["seconds_log"] = np.log(ufo['seconds'])

# Print out the variance of just the seconds_log column
print(ufo['seconds_log'].var())