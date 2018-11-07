'''In the video, you learned to write a function auc_train_test that calculates the AUC of model that is built on a train set and evaluated on a test set:

auc_train, auc_test = auc_train_test(variables, target, train, test)
with variables a list of the names of the variables that is used in the model.

In this exercise, you will apply this function, and check whether the train and test AUC are similar.'''
#TASK
# The basetable is loaded. Partition the basetable such that the train set contains 70% of the data, and make sure that train and test set have equal target incidence.
# Calculate the train and test AUC of the model using "age" and "gender_F" as predictors using the auc_train_test function.

# Load the partitioning module
from sklearn.cross_validation import train_test_split

# Create dataframes with variables and target
X = basetable.drop('target', 1)
y = basetable["target"]

# Carry out 70-30 partititioning with stratification
X_train, X_test, y_train, y_test = ____(X, y, test_size = ____, stratify = ____)

# Create the final train and test basetables
train = pd.concat([X_train, y_train], axis=1)
test = pd.concat([X_test, y_test], axis=1)

 # Apply the auc_train_test function
auc_train, auc_test = ____([____, ____], ["target"], ____, ____)
print(round(auc_train,2))
print(round(auc_test,2))






#SOLUTION
# Load the partitioning module
from sklearn.cross_validation import train_test_split

# Create dataframes with variables and target
X = basetable.drop('target', 1)
y = basetable["target"]

# Carry out 70-30 partititioning with stratification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, stratify = y)

# Create the final train and test basetables
train = pd.concat([X_train, y_train], axis=1)
test = pd.concat([X_test, y_test], axis=1)

 # Apply the auc_train_test function
auc_train, auc_test = auc_train_test(["age","gender_F"], ["target"], train, test)
print(round(auc_train,2))
print(round(auc_test,2))