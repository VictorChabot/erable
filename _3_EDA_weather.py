import plotly.express as px
import pandas as pd
import os

PATH_IN = os.path.join('data', 'df_weather_final_processed.pkl')
df = pd.read_pickle(PATH_IN)

def group_per_period(df:pd.DataFrame, col_period:str, cols_to_mean:[str]) -> pd.DataFrame:

    df_g = df.groupby(col_period)

    df_count = df_g[cols_to_mean].mean()

    return df_count


cols_to_mean = ['min_temp', 'max_temp', 'mean_temp', 'temp_diff']

cols_to_sum = ['temp_thaw', 'temp_frozen', 'temp_freeze_thaw', 'min_temp_thaw', 'max_temp_thaw', 'min_temp_freeze', 'max_temp_freeze', 'has_snow_on_grnd', 'snowed', 'rained']

total_cols = cols_to_mean + cols_to_sum

df_g = group_per_period(df=df, col_period=['month_of_year_p'], cols_to_mean=total_cols)
df_g = df_g.sort_index()

df_g.index = df_g.index.strftime('%Y-%m')

# df_g_month = group_per_period(df=df, col_period=['year', 'month'], cols_to_mean=total_cols)

def plot_columns(df, lst_cols):

    fig = px.line(df, x=df.index, y=lst_cols[0], hover_name=lst_cols[0])

    for temp_col in lst_cols[1:]:
        print(temp_col)
        fig.add_scatter(x=df.index, y=df[temp_col], name=temp_col)

    fig.show()

    return fig


fig_month = plot_columns(df=df_g, lst_cols=total_cols)


