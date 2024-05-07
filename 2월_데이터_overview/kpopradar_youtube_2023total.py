# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
# Importing all the Required Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode
import seaborn as sns
import datetime as dt
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns',None)
init_notebook_mode(connected=True)
# -

df=pd.read_csv('../original_data/KAIST_artists_daily_20230930.csv')

df

df['id'].unique().shape

df['name'].unique().shape

df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df

df_summed = df.groupby('date')['viewcount'].sum().reset_index()

df_summed

# Replace 'specified_date' with the date you want to compare against (in datetime format)
start_date = pd.to_datetime('2021-08-01') ### Change Here!
end_date = pd.to_datetime('2022-08-01')
df_summed_filtered = df_summed[(df_summed['date'] >= start_date) & (df_summed['date'] <= end_date)]
df_summed_filtered['viewcount'].sum()

# Replace 'specified_date' with the date you want to compare against (in datetime format)
start_date = pd.to_datetime('2022-08-01') ### Change Here!
end_date = pd.to_datetime('2023-08-01')
df_summed_filtered = df_summed[(df_summed['date'] >= start_date) & (df_summed['date'] <= end_date)]
df_summed_filtered['viewcount'].sum()

# Replace 'specified_date' with the date you want to compare against (in datetime format)
start_date = pd.to_datetime('2021-04-01') ### Change Here!
end_date = pd.to_datetime('2022-04-01')
df_summed_filtered = df_summed[(df_summed['date'] >= start_date) & (df_summed['date'] <= end_date)]
df_summed_filtered['viewcount'].sum()

# Replace 'specified_date' with the date you want to compare against (in datetime format)
start_date = pd.to_datetime('2022-04-01') ### Change Here!
end_date = pd.to_datetime('2023-04-01')
df_summed_filtered = df_summed[(df_summed['date'] >= start_date) & (df_summed['date'] <= end_date)]
df_summed_filtered['viewcount'].sum()


