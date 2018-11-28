'''Several python libraries provide convenient abstracted interfaces so that you need not always be so explicit in handling the machinery of optimization of the model.

As an example, in this exercise, you will use the statsmodels library in a more high-level, generalized work-flow for building a model using least-squares optimization (minimization of RSS).

To help get you started, we've pre-loaded the data from x_data, y_data = load_data() and stored it in a pandas DataFrame with column names x_column and y_column using 
df = pd.DataFrame(dict(x_column=x_data, y_column=y_data))'''
#TASK
# Construct a model ols() with formula formula="y_column ~ x_column" and data data=df, and then .fit() it to the data.
# Use model_fit.predict() to get y_model values and over-plot them with y_data.
# Extract the model parameter values a0 and a1 from model_fit.params.
# Use compute_rss_and_plot_fit() to confirm these results are consistent with the analytic formulae implemented with numpy.

# Pass data and `formula` into ols(), use and `.fit()` the model to the data
model_fit = ols(____="y_column ~ x_column", ____=df).____()

# Use .predict(df) to get y_model values, then over-plot y_data with y_model
y_model = model_fit.____(df)
fig = plot_data_with_model(x_data, ____, ____)

# Extract the a0, a1 values from model_fit.params
a0 = model_fit.____['Intercept']
a1 = model_fit.____['x_column']

# Visually verify that these parameters a0, a1 give the minimum RSS
fig, rss = compute_rss_and_plot_fit(a0, a1)




#SOLUTION
# Pass data and `formula` into ols(), use and `.fit()` the model to the data
model_fit = ols(formula="y_column ~ x_column", data=df).fit()

# Use .predict(df) to get y_model values, then over-plot y_data with y_model
y_model = model_fit.predict(df)
fig = plot_data_with_model(x_data, y_data, y_model)

# Extract the a0, a1 values from model_fit.params
a0 = model_fit.params['Intercept']
a1 = model_fit.params['x_column']

# Visually verify that these parameters a0, a1 give the minimum RSS
fig, rss = compute_rss_and_plot_fit(a0, a1)