'''The forward stepwise variable selection procedure provides an order in which variables are optimally added to the predictor set. 
In order to decide where to cut off the variables, you can make the train and test AUC curves. 
These curves plot the train and test AUC using the first, first two, first three, ... variables in the model.

In this exercise you will learn to plot these AUC curves. 
The method auc_train_test to calculate the AUC values has been implemented for you and can be used as follows:

auc_train, auc_test = auc_train_test(variables, target, train, test)
where variables is the set of variables used in the logistic regression model, target is a list with the target name, and train and test are the train and test basetable respectively.

The variables ordered according to the forward stepwise procedure are given in the list variables. 
You can explore it in the console. Additionally, three empty lists have been defined for you:

auc_values_train, which will contain the train AUC values of the model at each iteration
auc_values_test, which will contain the test AUC values of the model at each iteration
variables_evaluate, which will contain the variables evaluated at each iteration'''
#TASK
# Iterate over the variables.
# In each iteration, add the next variable in variables to variables_evaluate.
# In each iteration, calculate the train and test AUC using the auc_train_test method. The dataframes train and test contain the train and test data respectively.
# In each iteration, add the calculated values to auc_values_train and auc_values_test

# Keep track of train and test AUC values
auc_values_train = []
auc_values_test = []
variables_evaluate = []

# Iterate over the variables in variables
for v in ____:
  
    # Add the variable
    variables_evaluate.append(____)
    
    # Calculate the train and test AUC of this set of variables
    auc_train, auc_test = ____(____, ["target"], ____, ____)
    
    # Append the values to the lists
    auc_values_train.append(____)
    auc_values_test.append(____)
    
# Make plot of the AUC values
import matplotlib.pyplot as plt
import numpy as np

x = np.array(range(0,len(auc_values_train)))
y_train = np.array(auc_values_train)
y_test = np.array(auc_values_test)
plt.xticks(x, variables, rotation = 90)
plt.plot(x,y_train)
plt.plot(x,y_test)
plt.ylim((0.6, 0.8))
plt.show()






#SOLUTION
# Keep track of train and test AUC values
auc_values_train = []
auc_values_test = []
variables_evaluate = []

# Iterate over the variables in variables
for v in variables:
  
    # Add the variable
    variables_evaluate.append(v)
    
    # Calculate the train and test AUC of this set of variables
    auc_train, auc_test = auc_train_test(variables_evaluate, ["target"], train, test)
    
    # Append the values to the lists
    auc_values_train.append(auc_train)
    auc_values_test.append(auc_test)
    
# Make plot of the AUC values
import matplotlib.pyplot as plt
import numpy as np

x = np.array(range(0,len(auc_values_train)))
y_train = np.array(auc_values_train)
y_test = np.array(auc_values_test)
plt.xticks(x, variables, rotation = 90)
plt.plot(x,y_train)
plt.plot(x,y_test)
plt.ylim((0.6, 0.8))
plt.show()