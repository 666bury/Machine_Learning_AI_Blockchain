'''In the video you learned to implement a method that calculates the profit of a campaign:

profit = profit(perc_targets, perc_selected, population_size, campaign_cost, campaign_reward)

In this method, perc_targets is the percentage of targets in the group that you select for your campaign, 
perc_selected the percentage of people that is selected for the campaign, population_size the total population size, 
campaign_cost the cost of addressing a single person for the campaign, and campaign_reward the reward of addressing a target.

In this exercise you will learn for a specific case whether it is useful to use a model, 
by comparing the profit that is made when addressing all donors versus the top 40% of the donors.'''
#TASK
# Plot the lift curve. The predictions are in predictions_test and the true target values are in targets_test.
# Read the lift value at 40% and fill it out.
# The information about the campaign is filled out in the script. Calculate the profit made when addressing the entire population.
# Calculate the profit made when addressing the top 40%.

# Plot the lift graph
skplt.metrics.plot_lift_curve(____, ____)
plt.show()

# Read the lift at 40% (round it up to the upper tenth)
perc_selected = 0.4
lift = ____

# Information about the campaign
population_size, target_incidence, campaign_cost, campaign_reward = 100000, 0.01, 1, 100
    
# Profit if all donors are targeted
profit_all = profit(____, 1, population_size, campaign_cost, campaign_reward)
print(profit_all)

# Profit if top 40% of donors are targeted
profit_40 = profit(____ * ____, 0.4, population_size, campaign_cost, campaign_reward)
print(profit_40)





#SOLUTION
# Plot the lift graph
skplt.metrics.plot_lift_curve(targets_test, predictions_test)
plt.show()

# Read the lift at 40% (round it up to the upper tenth)
perc_selected = 0.4
lift = 1.5

# Information about the campaign
population_size, target_incidence, campaign_cost, campaign_reward = 100000, 0.01, 1, 100
    
# Profit if all donors are targeted
profit_all = profit(target_incidence, 1, population_size, campaign_cost, campaign_reward)
print(profit_all)

# Profit if top 40% of donors are targeted
profit_40 = profit(lift * target_incidence, 0.4, population_size, campaign_cost, campaign_reward)
print(profit_40)