'''The Length column in the hiking dataset is a column of strings, but contained in the column is the mileage for the hike. 
We're going to extract this mileage using regular expressions, and then use a lambda in Pandas to apply the extraction to the DataFrame.'''
#TASK
# Create a pattern that will extract numbers and decimals from text, using \d+ to get numbers and \. to get decimals, and pass it into re's compile function.
# Use re's match function to search the text, passing in the pattern and the length text.
# Use the matched mile's group() attribute to extract the matched pattern, making sure to match group 0, and pass it into float.
# Apply the return_mileage() function to the hiking["Length"] column.

# Write a pattern to extract numbers and decimals
def return_mileage(length):
    pattern = re.____(r"____")
    
    # Search the text for matches
    mile = re.____(____, ____)
    
    # If a value is returned, use group(0) to return the found value
    if mile is not None:
        return float(____)
        
# Apply the function to the Length column and take a look at both columns
hiking["Length_num"] = ____.apply(lambda row: ____)
print(hiking[["Length", "Length_num"]].head())







#SOLUTION
# Write a pattern to extract numbers and decimals
def return_mileage(length):
    pattern = re.compile(r"\d+\.\d+")
    
    # Search the text for matches
    mile = re.match(pattern, length)
    
    # If a value is returned, use group(0) to return the found value
    if mile is not None:
        return float(mile.group(0))
        
# Apply the function to the Length column and take a look at both columns
hiking["Length_num"] = hiking["Length"].apply(lambda row: return_mileage(row))
print(hiking[["Length", "Length_num"]].head())