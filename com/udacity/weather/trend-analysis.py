import pandas as pd

world_df = pd.read_csv('../../../data/world.csv')
world_series = pd.Series(data=world_df['avg_temp'].values, index=world_df['year'].values)

barcelona_df = pd.read_csv('../../../data/barcelona.csv')
barcelona_series = pd.Series(data=barcelona_df['avg_temp'].values, index=barcelona_df['year'].values)

frame = {"world": world_series, "Barcelona": barcelona_series}
df = pd.DataFrame(frame)