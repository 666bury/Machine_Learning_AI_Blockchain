'''In this exercise, you will use the function written previously to compute the RSS, and use it as an optimization constraint in the selection of specific parameter values that result in the model that best fits the data. We'll see that the values for the parameters we found earlier are precisely the ones needed to minimize the RSS.'''
#TASK
# Complete the function definition for compute_rss_and_plot_fit().
# Use compute_rss_and_plot_fit() compute RSS and plot the fit for trial values of a0 and a1.
# Vary the input slope a1 and intercept a0 until the model line fits the data and the RSS value is minimized.

# Complete function to load data, build model, compute RSS, and plot
def compute_rss_and_plot_fit(a0, a1):
    xd, yd = load_data()
    ym = model(xd, ____, ____)
    rss = compute_rss(____, ____)
    summary = "Parameters a0={}, a1={} yield RSS={:0.2f}".format(a0, a1, rss)
    fig = plot_data_with_model(xd, ____, ____, summary)
    return rss, summary

# Chose model parameter values and pass them into RSS function
rss, summary = compute_rss_and_plot_fit(a0=____, a1=____)
print(summary)






#SOLUTION
# Complete function to load data, build model, compute RSS, and plot
def compute_rss_and_plot_fit(a0, a1):
    xd, yd = load_data()
    ym = model(xd, a0, a1)
    rss = compute_rss(yd, ym)
    summary = "Parameters a0={}, a1={} yield RSS={:0.2f}".format(a0, a1, rss)
    fig = plot_data_with_model(xd, yd, ym, summary)
    return rss, summary

# Chose model parameter values and pass them into RSS function
rss, summary = compute_rss_and_plot_fit(a0=150, a1=25)
print(summary)