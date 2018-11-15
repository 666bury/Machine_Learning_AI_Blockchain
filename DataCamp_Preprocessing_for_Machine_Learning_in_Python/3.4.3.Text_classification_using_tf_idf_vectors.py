'''Now that we've encoded the volunteer dataset's title column into tf/idf vectors, let's use those vectors to try to predict the category_desc column.'''
#TASK
# Using train_test_split, split the text_tfidf vector, along with your y variable, into training and test sets. Set the stratify parameter equal to y, since the class distribution is uneven. Notice that we have to run the toarray() method on the tf/idf vector, in order to get in it the proper format for scikit-learn.
# Use Naive Bayes' fit() method on the train_X and train_y variables.
# Print out the score() of the test_X and test_y variables.

# Split the dataset according to the class distribution of category_desc
y = volunteer["category_desc"]
train_X, test_X, train_y, test_y = ____(____.toarray(), ____, ____=____)

# Fit the model to the training data
nb.____(____, ____)

# Print out the model's accuracy
print(nb.____(____, ____))




#SOLUTION
# Split the dataset according to the class distribution of category_desc
y = volunteer["category_desc"]
train_X, test_X, train_y, test_y = train_test_split(text_tfidf.toarray(), y, stratify=y)

# Fit the model to the training data
nb.fit(train_X, train_y)

# Print out the model's accuracy
print(nb.score(test_X, test_y))