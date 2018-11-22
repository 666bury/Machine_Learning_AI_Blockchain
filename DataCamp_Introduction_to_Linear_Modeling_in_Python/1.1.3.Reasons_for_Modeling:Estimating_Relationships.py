'''Another common application of modeling is to compare two data sets by building models for each, and then comparing the models. In this exercise, you are given data for a road trip two cars took together. The cars stopped for gas every 50 miles, but each car did not need to fill up the same amount, because the cars do not have the same fuel efficiency (MPG). Complete the function efficiency_model(miles, gallons) to estimate efficiency as average miles traveled per gallons of fuel consumed. Use the provided dictionaries car1 and car2, which both have keys car['miles'] and car['gallons'].'''
#TASK
# Complete the function definition for efficiency_model(miles, gallons)
# Use the function to compute the efficiency of the provided cars (dicts car1, car2)
# Store your answers as car1['mpg'] and car2['mpg'].
# Indicate which car has the best mpg by setting best_car=1, best_car=2, or best_car=0 if the same.

# Complete the function to model the efficiency.
def efficiency_model(miles, gallons):
   return np.mean( ____ / ____ )

# Use the function to estimate the efficiency for each car.
car1['mpg'] = efficiency_model( car1['____'] , car1['____'] )
car2['mpg'] = efficiency_model( car2['____'] , car2['____'] )

# Finish the logic statement to compare the car efficiencies.
if car1['mpg'] ____ car2['mpg'] :
    print('car1 is the best')
elif car1['mpg'] ____ car2['mpg'] :
    print('car2 is the best')
else:
    print('the cars have the same efficiency')







#SOLUTION
# Complete the function to model the efficiency.
def efficiency_model(miles, gallons):
   return np.mean(miles/gallons)

# Use the function to estimate the efficiency for each car.
car1['mpg'] = efficiency_model(car1['miles'], car1['gallons'])
car2['mpg'] = efficiency_model(car2['miles'], car2['gallons'])

# Finish the logic statement to compare the car efficiencies.
if car1['mpg'] > car2['mpg'] :
    print('car1 is the best')
elif car1['mpg'] < car2['mpg'] :
    print('car2 is the best')
else:
    print('the cars have the same efficiency')