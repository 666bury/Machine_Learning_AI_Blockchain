'''The predictions that result from the predictive model reflect how likely it is that someone is a target. 
For instance, assume that you constructed a model to predict whether a donor will donate more than 50 Euro for a certain campaign. 
If the prediction for a certain donor is 0.82, it means that there is an 82% chance that he will donate more than 50 Euro.

In this exercise you will find the donor that is most likely to donate more than 50 Euro.

Recall that you can sort a pandas dataframe df according to a certain column c using

df_sorted = df.sort(["c"])
and that you can select the first and last row of a pandas dataframe using

first_row = df.head(1)
last_row = df.tail(1)'''
#TASK
# The predictions are in a pandas dataframe predictions that has two columns: the donor ID and the probability to be target. Sort these predictions such that the donors with lowest probability to donate are first.
# Select and print the row in this sorted dataframe that has the donor that is most likely to donate more than 50 Euro according to the model.

# Sort the predictions
predictions_sorted = ____.____([____])

# Print the row of predictions_sorted that has the donor that is most likely to donate
print(____.____(____))



#SOLUTION
# Sort the predictions
predictions_sorted = predictions.sort(['probability'])

# Print the row of predictions_sorted that has the donor that is most likely to donate
print(predictions_sorted.tail(1))