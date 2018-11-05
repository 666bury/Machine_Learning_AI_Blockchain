'''It is always useful to get a better understanding of the population. 
Therefore, one can have a closer look at the predictive variables. 
Recall that you can select a column in a pandas dataframe by indexing as follows:

basetable["variable"]
To count the number of occurrences of a certain value in a column, you can use the sum method:

sum(basetable["variable"]==value)
In this exercise you will find out whether there are more males than females in the population.'''
#TASK
# Count and print the number of females.
# Count and print the number of males.

# Count and print the number of females.
print(____(____[____] == ____))

# Count and print the number of males.
print(____)






#SOLUTION
# Count and print the number of females.
print(sum(basetable['gender'] == "F"))

# Count and print the number of males.
print(sum(basetable['gender'] == "M"))