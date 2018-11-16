'''Let's re-run the Naive Bayes text classification model we ran at the end of chapter 3, 
with our selection choices from the previous exercise, 
on the volunteer dataset's title and category_desc columns.'''
#TASK
# Use train_test_split on the filtered_text text vector, the y labels (which is the category_desc labels), and pass the y set to the stratify parameter, since we have an uneven class distribution.
# Fit the nb Naive Bayes model to train_X and train_y.
# Score the nb model on the test_X and text_y test sets.

# Split the dataset according to the class distribution of category_desc, using the filtered_text vector
train_X, test_X, train_y, test_y = ____(____.toarray(), ____, stratify=____)

# Fit the model to the training data
nb.____

# Print out the model's accuracy
print(nb.____)








#SOLUTION
# Split the dataset according to the class distribution of category_desc, using the filtered_text vector
train_X, test_X, train_y, test_y = train_test_split(filtered_text.toarray(), y, stratify=y)

# Fit the model to the training data
nb.fit(train_X, train_y)

# Print out the model's accuracy
print(nb.score(test_X, test_y))