import pandas as pd

world_df = pd.read_csv('../../../data/world.csv')
world_series = pd.Series(data=world_df['avg_temp'].values, index=world_df['year'].values)
world_rolling_mean_series: pd.Series = world_series.rolling(10).mean().iloc[9:]

barcelona_df = pd.read_csv('../../../data/barcelona.csv')
barcelona_series: pd.Series = pd.Series(data=barcelona_df['avg_temp'].values, index=barcelona_df['year'].values)
barcelona_rolling_mean_series: pd.Series = barcelona_series.rolling(10).mean().iloc[9:]

frame = {"World": world_series,
         "World Rolling Mean (10)": world_rolling_mean_series,
         "Barcelona": barcelona_series,
         "Barcelona Rolling Mean (10)": barcelona_rolling_mean_series}
df = pd.DataFrame(frame)

df.to_csv('../../../data/output/data.csv', sep='|', float_format='%.2f', decimal=',')