'''In order to make predictor insight graphs for continuous variables, you first need to discretize them. 
In Python, you can discretize pandas columns using the qcut method.

To check whether the variable was nicely discretized, you can verify that the bins have equal size using the groupby method:

print(basetable.groupby("discretized_variable").size()'''
#TASK
# Use the method qcut to discretize the variable time_since_last_donation in 10 groups. Assing this variable to a new column called "bins_recency".
# Use the method groupby to verify that the bins have about equal size.

# Discretize the variable time_since_last_donation in 10 bins
basetable["bins_recency"] = pd.qcut(____,____)

# Print the group sizes of the discretized variable
print(basetable.groupby("____").size())




#SOLUTION
# Discretize the variable time_since_last_donation in 10 bins
basetable["bins_recency"] = pd.qcut(basetable["time_since_last_donation"], 10)

# Print the group sizes
print(basetable.groupby("bins_recency").size())