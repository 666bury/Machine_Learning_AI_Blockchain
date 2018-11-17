'''The length_of_time field in the UFO dataset is a text field that has the number of minutes within the string. 
Here, you'll extract that number from that text field using regular expressions.'''
#TASK
# Pass \d+ into re.compile() in the pattern variable to designate that we want to grab as many digits as possible from the string.
# Into re.match(), pass the pattern we just created, as well as the time_string we want to extract from.
# Use lambda within the apply() method to perform the extraction.
# Print out the head() of both the length_of_time and minutes columns to compare.

def return_minutes(time_string):

    # Use \d+ to grab digits
    pattern = re.____(r"____")
    
    # Use match on the pattern and column
    num = re.____(____, ____)
    if num is not None:
        return int(num.group(0))
        
# Apply the extraction to the length_of_time column
ufo["minutes"] = ufo["length_of_time"].____

# Take a look at the head of both of the columns
print(ufo[[____]].head())



#SOLUTION
def return_minutes(time_string):
    
    # We'll use \d+ to grab digits and match it to the column values
    pattern = re.compile(r"\d+")
        
    # Use match on the pattern and column
    num = re.match(pattern, time_string)
    if num is not None:
        return int(num.group(0))
        
# Apply the extraction to the length_of_time column
ufo["minutes"] = ufo["length_of_time"].apply(return_minutes)

# Take a look at the head of both of the columns
print(ufo[["length_of_time", "minutes"]].head())