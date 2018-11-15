'''Take a look at the hiking dataset. 
There are several columns here that need encoding, one of which is the Accessible column, which needs to be encoded in order to be modeled. 
Accessible is a binary feature, so it has two values - either Y or N - so it needs to be encoded into 1s and 0s. 
Use scikit-learn's LabelEncoder method to do that transformation.'''
#TASK
# Store LabelEncoder() in a variable named enc
# Using the encoder's fit_transform() function, encode the hiking dataset's "Accessible" column. Call the new column Accessible_enc.
# Compare the two columns side-by-side to see the encoding.

# Set up the LabelEncoder object
enc = ____

# Apply the encoding to the "Accessible" column
____ = ____.____(____)

# Compare the two columns
print(____[[____, ____]].head())






#SOLUTION
# Set up the LabelEncoder object
enc = LabelEncoder()

# Apply the encoding to the "Accessible" column
hiking['Accessible_enc'] = enc.fit_transform(hiking['Accessible'])

# Compare the two columns
print(hiking[['Accessible', 'Accessible_enc']].head())