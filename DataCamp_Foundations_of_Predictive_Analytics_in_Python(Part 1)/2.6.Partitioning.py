'''In order to properly evaluate a model, one can partition the data in a train and test set. 
The train set contains the data the model is built on, and the test data is used to evaluate the model. 
This division is done randomly, but when the target incidence is low, it could be necessary to stratify, that is, to make sure that the train and test data contain an equal percentage of targets.

In this exercise you will partition the data with stratification and verify that the train and test data have equal target incidence. 
The train_test_split method has already been imported, and the X and y dataframes are available in your workspace.'''
#TASK
# Stratify these dataframes using the train_test_split method. Make sure that train and test set are the same size, and have equal target incidence.
# Calculate the target incidence of the train set. This is the number of targets in the train set divided by the number of observations in the train set.
# Calculate the target incidence of the test set.

# Load the partitioning module
from sklearn.cross_validation import train_test_split

# Create dataframes with variables and target
X = basetable.drop("target", 1)
y = basetable["target"]

# Carry out 50-50 partititioning with stratification
X_train, X_test, y_train, y_test = ____(X, y, test_size = ____, stratify = ____)

# Create the final train and test basetables
train = pd.concat([X_train, y_train], axis=1)
test = pd.concat([X_test, y_test], axis=1)

# Check whether train and test have same percentage targets
print(round(sum(train[____])/len(____), 2))
print(round(sum(test[____])/len(____), 2))






#SOLUTION
# Load the partitioning module
from sklearn.cross_validation import train_test_split

# Create dataframes with variables and target
X = basetable.drop('target', 1)
y = basetable["target"]

# Carry out 50-50 partititioning with stratification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.50, stratify = y)

# Create the final train and test basetables
train = pd.concat([X_train, y_train], axis=1)
test = pd.concat([X_test, y_test], axis=1)

# Check whether train and test have same percentage targets
print(round(sum(train["target"])/len(train), 2))
print(round(sum(test["target"])/len(test), 2))