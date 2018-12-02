'''In Part 1, you computed a single log-likelihood for a single mu. In this Part 2, you will apply the predefined function compute_loglikelihood(), to compute an array of log-likelihood values, one for each element in an array of possible mu values.

The goal then is to determine which single mu guess leads to the single maximum value of the loglikelihood array.

To get started, use the preloaded data sample_distances, sample_mean, sample_stdev and a helper function compute_loglikelihood()'''
#TASK
# Construct mu_guesses, by taking values centered on sample_mean and spread by sample_stdev.
# For each guess value in mu_guesses, use compute_loglikelihood() for all sample_distances, holding sigma fixed at sample_stdev.
# From the loglikelihoods array, find the maximum value, and use its index to find the best_mu from our mu_guesses.
# Print the best_mu and visualize it by plotting the loglikelihoods.

# Create an array of mu guesses, centered on sample_mean, spread out +/- by sample_stdev
low_guess = sample_mean - 2*sample_stdev
high_guess = sample_mean + 2*sample_stdev
mu_guesses = np.linspace(____, ____, 101)

# Compute the loglikelihood for each model created from each guess value
loglikelihoods = np.zeros(len(mu_guesses))
for n, mu_guess in enumerate(____):
    loglikelihoods[n] = compute_loglikelihood(____, mu=____, sigma=sample_stdev)

# Find the best guess by using logical indexing, the print and plot the result
best_mu = mu_guesses[loglikelihoods==np.max(____)]
print('Maximum loglikelihood found for best mu guess={}'.format(____))
fig = plot_loglikelihoods(mu_guesses, loglikelihoods)









#SOLUTION
# Create an array of mu guesses, centered on sample_mean, spread out +/- by sample_stdev
low_guess = sample_mean - 2*sample_stdev
high_guess = sample_mean + 2*sample_stdev
mu_guesses = np.linspace(low_guess, high_guess, 101)

# Compute the loglikelihood for each model created from each guess value
loglikelihoods = np.zeros(len(mu_guesses))
for n, mu_guess in enumerate(mu_guesses):
    loglikelihoods[n] = compute_loglikelihood(sample_distances, mu=mu_guess, sigma=sample_stdev)

# Find the best guess by using logical indexing, the print and plot the result
best_mu = mu_guesses[loglikelihoods==np.max(loglikelihoods)]
print('Maximum loglikelihood found at mu guess={}'.format(best_mu))
fig = plot_loglikelihoods(mu_guesses, loglikelihoods)


