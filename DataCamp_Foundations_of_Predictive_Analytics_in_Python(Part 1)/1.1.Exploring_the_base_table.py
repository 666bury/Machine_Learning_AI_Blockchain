'''Before diving into model building, it is important to understand the data you are working with. 
In this exercise, you will learn how to obtain the population size, number of targets and target incidence from a given basetable.'''
#TASK
# The basetable is loaded in a pandas object basetable. Assign the number of rows to the variable population_size and print it.
# Assign the number of targets equal to one to the variable targets_count and print it.
# Print the target incidence, this is the ratio of targets_count and population_size.

# Assign the number of rows in the basetable to the variable 'population_size'.
population_size  = ____(____)

# Print the population size.
print(____)

# Assign the number of targets to the variable 'targets_count'.
targets_count = ____(____[____])

# Print the number of targets.
print(____)

# Print the target incidence.
print(____ / ____)



#SOLUTION
# Assign the number of rows in the basetable to the variable 'population_size'.
population_size  = len(basetable)

# Print the population size.
print(population_size)

# Assign the number of targets to the variable 'targets_count'.
targets_count = sum(basetable['target'])

# Print the number of targets.
print(targets_count)

# Print the target incidence.
print(targets_count / population_size)
