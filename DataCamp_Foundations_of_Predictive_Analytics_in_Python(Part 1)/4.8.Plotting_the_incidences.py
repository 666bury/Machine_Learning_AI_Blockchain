'''The most important element of the predictor insight graph are the incidence values. 
For each group in the population with respect to a given variable, the incidence values reflect the percentage of targets in that group. 
In this exercise, you will write a python function that plots the incidence values of a variable, given the predictor insight graph table.'''
#TASK
# Select the right column in the predictor insight graph table and plot this column.

import matplotlib.pyplot as plt
import numpy as np

# The function to plot a predictor insight graph.
def plot_incidence(pig_table,variable):
    
    # Plot the incidence line
    ____["____"].plot()
    
    # Formatting the predictor insight graph
    plt.xticks(np.arange(len(pig_table)), pig_table[variable])
    plt.xlim([-0.5, len(pig_table) - 0.5])
    plt.ylim([0, max(pig_table["Incidence"]*2)])
    plt.ylabel("Incidence", rotation = 0, rotation_mode="anchor", ha = "right")
    plt.xlabel(variable)
    
    # Show the graph
    plt.show()



#SOLUTION
# The function to plot a predictor insight graph.
def plot_incidence(pig_table,variable):
    
    # Plot the incidence line
    pig_table["Incidence"].plot()
    
    # Formatting the predictor insight graph
    plt.xticks(np.arange(len(pig_table)), pig_table[variable])
    plt.xlim([-0.5, len(pig_table) - 0.5])
    plt.ylim([0, max(pig_table["Incidence"]*2)])
    plt.ylabel("Incidence", rotation = 0, rotation_mode="anchor", ha = "right")
    plt.xlabel(variable)
    
    # Show the graph
    plt.show()

# Apply the function for the variable "country".
plot_incidence(pig_table, "country")