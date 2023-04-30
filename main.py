# %%
import pandas as pd

# %%
df = pd.read_csv(r'./data/uber_data.csv')
df.head()
# %%
df.info()
# %%
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
# %%
df.info()
# %%
df = df.drop_duplicates().reset_index(drop=True)
df['trip_id'] = df.index
# %%
df.head()
