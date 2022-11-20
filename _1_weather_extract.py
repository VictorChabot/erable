import pandas as pd
import os
import plotly.express as px

PATH_WEATHER = os.path.join('data', 'weather_raw')

def extract_load(path: str) -> pd.DataFrame:

    file_list = os.listdir(path)

    file_list = [file for file in file_list if file.endswith('.csv')]

    path = PATH_WEATHER

    lst_df = list()
    for file in file_list:

        temp_path = os.path.join(path, file)

        temp_df = pd.read_csv(temp_path)

        lst_df.append(temp_df)

    df = pd.concat(lst_df, axis=0)

    return df


df = extract_load(PATH_WEATHER)


df['datetime'] = pd.to_datetime(df['Date/Time'])

new_cols = [col.replace(' ', '_').lower() for col in df.columns]

df.columns = new_cols

cols_to_rename = {
'max_temp_(°c)': 'max_temp',
'min_temp_(°c)': 'min_temp',
'mean_temp_(°c)': 'mean_temp',
'total_rain_(mm)': 'total_rain',
'total_snow_(cm)': 'total_snow',
'total_precip_(mm)': 'total_precip',
'snow_on_grnd_(cm)': 'snow_on_grnd',

}

df = df.rename(cols_to_rename, axis=1)

cols_to_keep = ['station_name', 'datetime', 'year', 'month', 'day', 'min_temp', 'max_temp', 'mean_temp', 'total_rain', 'total_snow', 'total_precip', 'snow_on_grnd']


df = df.dropna(subset=['min_temp'])

df = df.loc[ :,  cols_to_keep]
df = df.sort_values('datetime')

df.to_pickle(os.path.join('data', 'df_weather_total.pkl'))

df = df.sort_values('station_name', ascending=False)

df = df.drop_duplicates(subset=['datetime'], keep='first')
df = df.sort_values('datetime', ascending=True)

df.to_pickle(os.path.join('data', 'df_weather_final.pkl'))
