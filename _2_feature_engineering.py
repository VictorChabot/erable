import pandas as pd
import os

PATH_IN = os.path.join('data', 'df_weather_final.pkl')
PATH_OUT = os.path.join('data', 'df_weather_final_processed.pkl')

df = pd.read_pickle(PATH_IN)

######## Date

df['day_of_year'] = df['datetime'].dt.isocalendar().day
df['week_of_year'] = df['datetime'].dt.isocalendar().week

df['month_of_year_p'] = df['datetime'].dt.to_period('M')
df['week_of_year_p'] = df['datetime'].dt.to_period('W')
df['2week_of_year_p'] = df['datetime'].dt.to_period('2W')
df['year_p']  = df['datetime'].dt.to_period('Y')

###### Weather Variation and thaw-freeze

df['temp_diff'] = df['max_temp'] - df['min_temp']

df['min_temp_thaw'] = 0 <= df['min_temp']
df['max_temp_thaw'] = 0 <= df['max_temp']
df['min_temp_freeze'] = df['min_temp'] <= -1
df['max_temp_freeze'] = df['max_temp'] <= -1

df['temp_freeze_thaw'] = (df['min_temp_freeze'] == True) & (df['max_temp_thaw'] == True)

df['temp_thaw'] = (df['min_temp_thaw'] == True) & (df['max_temp_thaw'] == True)
df['temp_frozen'] = (df['min_temp_freeze'] == True) & (df['max_temp_freeze'] == True)

###### Precipitation

df['has_snow_on_grnd'] = df['snow_on_grnd'] > 0
df['snowed'] = df['total_rain'] > 0
df['rained'] = df['total_rain'] > 0
df['had_precip'] = df['total_precip'] > 0

df['snowed_rained'] = (df['snowed']==True) & (df['rained']==True)

df['has_snow_on_grnd_&_snowed'] = (df['has_snow_on_grnd']==True) & (df['snowed']==True)
df['has_snow_on_grnd_&_rained'] = (df['has_snow_on_grnd']==True) & (df['rained']==True)
df['has_snow_on_grnd_&_snowed_rained'] = (df['has_snow_on_grnd']==True) & (df['snowed_rained']==True)
df['has_snow_on_grnd_&_had_precip'] = (df['has_snow_on_grnd']==True) & (df['had_precip']==True)



################

df.to_pickle(PATH_OUT)



################## Find Start of the season

# Keep pertinent months
# START_MONTH = 3
# END_MONTH = 5
#
# df = df.loc[df['month'].between(START_MONTH, END_MONTH)]

# COUNT DAYS PER WEEK/MONTH





