'''Let's first take a look at the accuracy of a K-nearest neighbors model on the wine dataset without standardizing the data. 
The knn model as well as the X and y data and labels sets have been created already. 
Most of this process of creating models in scikit-learn should look familiar to you.'''
#TASK
# Split the dataset into training and test sets using train_test_split().
# Use the knn model's fit() method on the X_train data and y_train labels, to fit the model to the data.
# Print out the knn model's score() on the X_test data and y_test labels to evaluate the model.

# Split the dataset and labels into training and test sets
X_train, X_test, y_train, y_test = ____

# Fit the k-nearest neighbors model to the training data
____.____(____, ____)

# Score the model on the test data
print(____.____(____, ____))








#SOLUTION
# Split the dataset and labels into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y)

# Fit the k-nearest neighbors model to the training data
knn.fit(X_train, y_train)

# Score the model on the test data
print(knn.score(X_test, y_test))