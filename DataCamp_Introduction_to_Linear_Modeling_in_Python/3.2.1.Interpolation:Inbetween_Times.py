'''In this exercise, you will build a linear model by fitting monthly time-series data for the Dow Jones Industrial Average (DJIA) and then use that model to make predictions for daily data (in effect, an interpolation). Then you will compare that daily prediction to the real daily DJIA data.

A few notes on the data. "OHLC" stands for "Open-High-Low-Close", which is usually daily data, for example the opening and closing prices, and the highest and lowest prices, for a stock in a given day. "DayCount" is an integer number of days from start of the data collection.'''
#TASK
# Use ols() to .fit() a model to the data=df_monthly with formula="Close ~ DayCount".
# Use model_fit.predict() on both df_monthly.DayCount and df_daily.DayCount to predict values for the monthly and daily Close prices, stored as a new column Model in each DataFrame.
# Use the predefined plot_model_with_data twice, on each df_monthly and df_daily and compare the RSS values shown.

# build and fit a model to the df_monthly data
model_fit = ols('Close ~ DayCount', ____=df_monthly).____()

# Use the model FIT to the MONTHLY data to make a predictions for both monthly and daily data
df_monthly['Model'] = model_fit.____(df_monthly.____)
df_daily['Model'] = model_fit.____(df_daily.____)

# Plot the monthly and daily data and model, compare the RSS values seen on the figures
fig_monthly = plot_model_with_data(____)
fig_daily = plot_model_with_data(____)






#SOLUTION
# fit a model to the df_monthly data
model_fit = ols('Close ~ DayCount', data=df_monthly).fit()

# Use the model to make a predictions for both monthly and daily data
df_monthly['Model'] = model_fit.predict(df_monthly.DayCount)
df_daily['Model'] = model_fit.predict(df_daily.DayCount)

# Plot model-to-data comparisons for both the monthly and daily, compare the RSS values
fig_monthly = plot_model_with_data(df_monthly)
fig_daily = plot_model_with_data(df_daily)