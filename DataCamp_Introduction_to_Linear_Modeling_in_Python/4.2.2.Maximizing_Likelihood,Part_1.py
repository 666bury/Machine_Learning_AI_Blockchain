'''Previously, we chose the sample mean as an estimate of the population model paramter mu. But how do we know that the sample mean is the best estimator? This is tricky, so let's do it in two parts.

In Part 1, you will use a computational approach to compute the log-likelihood of a given estimate. Then, in Part 2, we will see that when you compute the log-likelihood for many possible guess values of the estimate, one guess will result in the maximum likelihood.'''
#TASK
# Compute the mean() and std() of the preloaded sample_distances as the guessed values of the probability model parameters.
# Compute the probability, for each distance, using gaussian_model() built from sample_mean and sample_stdev
# Compute the loglikelihood as the sum() of the log() of the probabilities probs

# Compute sample mean and stdev, for use as model parameter value guesses
mu_guess = np.____(sample_distances)
sigma_guess = np.____(sample_distances)

# For each sample distance, compute the probability modeled by the parameter guesses
probs = np.zeros(len(sample_distances))
for n, distance in enumerate(sample_distances):
    probs[n] = gaussian_model(____, mu=____, sigma=____)

# Compute and print the log-likelihood as the sum() of the log() of the probabilities
loglikelihood = np.____(np.____(probs))
print('For guesses mu={:0.2f} and sigma={:0.2f}, the loglikelihood={:0.2f}'.format(mu_guess, sigma_guess, ____))





#SOLUTION
# Compute sample mean and stdev, for use as model parameter value guesses
mu_guess = np.mean(sample_distances)
sigma_guess = np.std(sample_distances)

# For each sample distance, compute the probability modeled by the parameter guesses
probs = np.zeros(len(sample_distances))
for n, distance in enumerate(sample_distances):
    probs[n] = gaussian_model(distance, mu=mu_guess, sigma=sigma_guess)

# Compute and print the log-likelihood as the sum() of the log() of the probabilities
loglikelihood = np.sum(np.log(probs))
print('For guesses mu={:0.2f} and sigma={:0.2f}, the loglikelihood={:0.2f}'.format(mu_guess, sigma_guess, loglikelihood))
