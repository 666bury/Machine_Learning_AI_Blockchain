'''Finally, let's build a model using the text vector we created, desc_tfidf, using the filtered_words list to create a filtered text vector. 
Let's see if we can predict the type of the sighting based on the text. 
We'll use a Naive Bayes model for this.'''
#TASK
# On the desc_tfidf vector, filter by passing a list of filtered_words into the index.
# Split up the X and y sets using train_test_split(). Remember to convert filtered_text using toarray(). Pass the y set to the stratify= parameter, since we have imbalanced classes here.
# Use the nb model's fit() to fit train_X and train_y.
# Print out the .score() of the nb model on the test_X and test_y sets.

# Use the list of filtered words we created to filter the text vector
filtered_text = ____[:, list(____)]

# Split the X and y sets using train_test_split, setting stratify=y 
train_X, test_X, train_y, test_y = ____(____.toarray(), ____, ____)

# Fit nb to the training sets
____

# Print the score of nb on the test sets
____








#SOLUTION
# Use the list of filtered words we created to filter the text vector
filtered_text = desc_tfidf[:, list(filtered_words)]

# Split the X and y sets using train_test_split, setting stratify=y 
train_X, test_X, train_y, test_y = train_test_split(filtered_text.toarray(), y, stratify=y)

# Fit nb to the training sets
nb.fit(train_X, train_y)

# Print the score of nb on the test sets
print(nb.score(test_X, test_y))