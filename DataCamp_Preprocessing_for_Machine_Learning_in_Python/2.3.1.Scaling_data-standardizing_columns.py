'''Since we know that the Ash, Alcalinity of ash, and Magnesium columns in the wine dataset are all on different scales, 
let's standardize them in a way that allows for use in a linear model.'''
#TASK
# Import StandardScaler from sklearn.preprocessing.
# Create the StandardScaler() method and store in a variable named ss.
# Create a subset of the wine DataFrame of the Ash, Alcalinity of ash, and Magnesium columns, store in a variable named wine_subset.
# Apply the ss.fit_transform method to the wine_subset DataFrame.

# Import StandardScaler from scikit-learn
from sklearn.preprocessing import ____

# Create the scaler
ss = ____

# Take a subset of the DataFrame you want to scale 
____ = wine[[____]]

# Apply the scaler to the DataFrame subset
wine_subset_scaled = ss.____(____)





#SOLUTION
# Import StandardScaler from scikit-learn
from sklearn.preprocessing import StandardScaler

# Create the scaler
ss = StandardScaler()

# Take a subset of the DataFrame you want to scale 
wine_subset = wine[['Ash', 'Alcalinity of ash', 'Magnesium']]

# Apply the scaler to the DataFrame subset
wine_subset_scaled = ss.fit_transform(wine_subset)