'''The qcut method divides the variable in n_bins equal bins. 
In some cases, however, it is nice to choose your own bins. 
The method cut in python allows you to choose your own bins.'''
#TASK
# Discretize the variable number_gift in three bins with borders 0 and 5, 5 and 10, 10 and 20 and assign this variable to a new column called disc_number_gift.
# Count the number of observations in each group.

# Discretize the variable 
basetable["disc_number_gift"] = pd.cut(____[____],[____, ____, ____, ____])

# Count the number of observations per group
print(basetable.groupby("____").____())





#SOLUTION
