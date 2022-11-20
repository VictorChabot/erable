import pandas as pd
import os
import plotly.express as px

df = pd.read_pickle(os.path.join('data', 'df_weather_final.pkl'))


fig = px.line(df, x='datetime', y='mean_temp')

fig.add_scatter(x=df['datetime'], y=df['min_temp'], mode='lines')
fig.add_scatter(x=df['datetime'], y=df['max_temp'], mode='lines')

fig.show()