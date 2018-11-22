'''Another common use of modeling extrapolation to estimate data values "outside" or "beyond" the range (min and max values of time) of the measured data. 
In this exercise, we have measured distances for times 0 through 5 hours, but we are interested in estimating how far we'd go in 8 hours. 
Using the same data set from the previous exercise, we have prepared a linear model distance = model(time). 
Use that model() to make a prediction about the distance traveled for a time much larger than the other times in the measurements.'''
#TASK
# Use distance = model(time=8) to extrapolate beyond the measured data.
# If your car can travel 400 miles on a full tank, and it takes 8 hours to drive home, will you make it without refilling?
# Set answer=True if you'll make it, or answer=False if you will run out of gas.

# Select a time not measured.
time = 8

# Use the model to compute a predicted distance for that time.
distance = model(____)

# Inspect the value of the predicted distance traveled.
print(distance)

# Determine if you will make it without refueling.
answer = (____ > 400)
print(answer)




#SOLUTION
# Select a time not measured.
time = 8

# Use the model to compute a predicted distance for that time.
distance = model(time=8)

# Inspect the value of the predicted distance traveled.
print(distance)

# Determine if you will make it without refueling.
answer = (distance >= 400)
print(answer)