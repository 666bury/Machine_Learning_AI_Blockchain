'''Now that we have run PCA on the wine dataset, let's try training a model with it.'''
#TASK
# Split the transformed_X vector and the y labels set into training and test sets using train_test_split.
# Fit the knn model using the fit() function on the X_wine_train and y_wine_train sets.
# Print out the score using knn's score() function on X_wine_test and y_wine_test.

# Split the transformed X and the y labels into training and test sets
X_wine_train, X_wine_test, y_wine_train, y_wine_test = ____

# Fit knn to the training data
____

# Score knn on the test data and print it out
____






#SOLUTION
# Split the transformed X and the y labels into training and test sets
X_wine_train, X_wine_test, y_wine_train, y_wine_test = train_test_split(transformed_X, y)

# Fit knn to the training data
knn.fit(X_wine_train, y_wine_train)

# Score knn on the test data and print it out
print(knn.score(X_wine_test, y_wine_test))