'''Let's apply PCA to the wine dataset, to see if we can get an increase in our model's accuracy.'''
#TASK
# Set up the PCA object. You'll use PCA on the wine dataset minus its label for Type, stored in the variable wine_X.
# Apply PCA to wine_X using pca's fit_transform method and store the transformed vector in transformed_X.
# Print out the explained_variance_ratio_ attribute of pca to check how much variance is explained by each component.

from sklearn.decomposition import PCA

# Set up PCA and the X vector for diminsionality reduction
pca = ____()
wine_X = wine.drop("Type", axis=1)

# Apply PCA to the wine dataset X vector
transformed_X = ___.____(____)

# Look at the percentage of variance explained by the different components
print(____)






#SOLUTION
from sklearn.decomposition import PCA

# Set up PCA and the X vector for diminsionality reduction
pca = PCA()
wine_X = wine.drop("Type", axis=1)

# Apply PCA to the wine dataset X vector
transformed_X = pca.fit_transform(wine_X)

# Look at the percentage of variance explained by the different components
print(pca.explained_variance_ratio_)