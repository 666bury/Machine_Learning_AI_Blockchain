'''Intuitively, we can look at the plots provided and "see" whether the two variables seem to "vary together".

Data Set A: x and y change together and appear to have a strong relationship.
Data Set B: there is a rough upward trend; x and y appear only loosely related.
Data Set C: looks like random scatter; x an y do not appear to change together and are unrelated.

In this exercise you will compare the 3 data sets by computing correlation, and determining which data set has the most strongly correlated variables x and y. Use the provided data table data_sets, a dictionary of records, each having keys 'name', 'x', 'y', and 'correlation'.'''
#TASK
# Complete the function definition for correlation() using the mean of the products of the normalized deviations of x and y.
# Iterate over data_sets, computing and storing correlation as record['correlation'] = correlation(record['x'], record['y']) for each.
# Assign the name of the dataset with strongest correlation to the variable best_data

# Complete the function that will compute correlation.
def correlation(x,y):
    x_dev = x - np.____(x)
    y_dev = y - np.____(y)
    x_norm = x_dev / np.____(x)
    y_norm = y_dev / np.____(y)
    return np.____(x_norm * y_norm)

# Compute and store the correlation for each data set in the list.
for name, data in data_sets.items():
    data['correlation'] = ____(data['x'], data['y'])
    print('data set {} has correlation {:.2f}'.format(name, data['correlation']))

# Assign the data set with the best correlation.
best_data = data_sets['____']







#SOLUTION
# Complete the function that will compute correlation.
def correlation(x,y):
    x_dev = x - np.mean(x)
    y_dev = y - np.mean(y)
    x_norm = x_dev / np.std(x)
    y_norm = y_dev / np.std(y)
    return np.mean(x_norm * y_norm)

# Compute and store the correlation for each data set in the list.
for name, data in data_sets.items():
    data['correlation'] = correlation(data['x'], data['y'])
    print('data {} has correlation {}'.format(name, data['correlation']))

# Assign the data set with the best correlation.
best_data = data_sets['A']

