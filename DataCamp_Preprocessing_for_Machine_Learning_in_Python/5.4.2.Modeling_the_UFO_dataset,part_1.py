'''In this exercise, we're going to build a k-nearest neighbor model to predict which country the UFO sighting took place in. 
Our X dataset has the log-normalized seconds column, the one-hot encoded type columns, as well as the month and year when the sighting took place. 
The y labels are the encoded country column, where 1 is us and 0 is ca.'''
#TASK
# Print out the .columns of the X set.
# Split up the X and y sets using train_test_split(). Pass the y set to the stratify= parameter, since we have imbalanced classes here.
# Use fit() to fit train_X and train_y.
# Print out the .score() of the knn model on the test_X and test_y sets.

# Take a look at the features in the X set of data
print(____)

# Split the X and y sets using train_test_split, setting stratify=y
train_X, test_X, train_y, test_y = ____

# Fit knn to the training sets
knn.____

# Print the score of knn on the test sets
print(____)




#SOLUTION
# Take a look at the features in the X set of data
print(X.columns)

# Split the X and y sets using train_test_split, setting stratify=y
train_X, test_X, train_y, test_y = train_test_split(X, y, stratify=y)

# Fit knn to the training sets
knn.fit(train_X, train_y)

# Print the score of knn on the test sets
print(knn.score(test_X, test_y))