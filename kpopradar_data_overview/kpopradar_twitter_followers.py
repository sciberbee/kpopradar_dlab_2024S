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

df=pd.read_csv('../original_data/KAIST_kpopradar_instagram_20230930.csv')

df.head()

df.info()

# +
# Get specified data for BLACKPINK artist_name, type conversion of 'date' column to datetime

BLACKPINK_df = df[df['artist_name'] == 'BLACKPINK'].sort_values('date')
BLACKPINK_df['date'] = pd.to_datetime(BLACKPINK_df['date'], format='%Y%m%d')
BLACKPINK_df
# -

from matplotlib.ticker import ScalarFormatter, MaxNLocator
import matplotlib.dates as mdates

# +
# Replace 'specified_date' with the date you want to compare against (in datetime format)
start_date = pd.to_datetime('2019-09-01') ### Change Here!
end_date = pd.to_datetime('2021-04-01')
quantity_name = 'followers' ### Type the column name of desired quantity!

# Filter the DataFrame to get rows with date greater than specified_date
filtered_BLACKPINK_df = BLACKPINK_df[(BLACKPINK_df['date'] > start_date) & (BLACKPINK_df['date'] < end_date)]

plt.figure(figsize = (15,8))
plt.plot(filtered_BLACKPINK_df['date'], filtered_BLACKPINK_df[quantity_name])

# Apply ScalarFormatter to the y-axis (subscriber_count)
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=False))
plt.ticklabel_format(style='plain', axis='y')  # Another way to disable scientific notation

plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# Show grid
plt.grid(True)
# Fill between the graph and x axis
plt.fill_between(filtered_BLACKPINK_df['date'],filtered_BLACKPINK_df[quantity_name],alpha=0.5) # alpha : 투명도 

plt.title('BLACKPINK Twitter' + ' ' + quantity_name)
plt.xlabel('Date')
plt.ylabel('Subscriber Count')

plt.show()

# +
#Combining two graph
# -

df_yousub = pd.read_csv('../original_data/KAIST_kpopradar_youtube_channel_20230930.csv')

df_yousub = df_yousub[df_yousub['artist_name'] == 'BLACKPINK'].sort_values('date')
df_yousub['date'] = pd.to_datetime(df_yousub['date'], format='%Y%m%d')
df_yousub

# +
# Replace 'specified_date' with the date you want to compare against (in datetime format)
start_date = pd.to_datetime('2019-09-01') ### Change Here!
end_date = pd.to_datetime('2021-04-01')
quantity_name = 'followers' ### Type the column name of desired quantity!
quantity_name2 = 'subscriber_count'

# Filter the DataFrame to get rows with date greater than specified_date
filtered_BLACKPINK_df = BLACKPINK_df[(BLACKPINK_df['date'] > start_date) & (BLACKPINK_df['date'] < end_date)]

filtered_BLACKPINK_yousub_df = df_yousub[(df_yousub['date'] > start_date) & (df_yousub['date'] < end_date)]

plt.figure(figsize = (15,8))
plt.plot(filtered_BLACKPINK_df['date'], filtered_BLACKPINK_df[quantity_name], label = quantity_name, color = 'skyblue')
plt.plot(filtered_BLACKPINK_yousub_df['date'], filtered_BLACKPINK_yousub_df[quantity_name2], label = quantity_name2, color = 'red')
# You Can Specify the Label of each plot

# Apply ScalarFormatter to the y-axis (subscriber_count)
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=False))
plt.ticklabel_format(style='plain', axis='y')  # Another way to disable scientific notation

plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# Show grid
plt.grid(True)

# Show the Legend
plt.legend()

plt.title('BLACKPINK' + ' ' + 'Twitter ' + quantity_name + ' and ' + 'YouTube ' + quantity_name2)
plt.xlabel('Date')
plt.ylabel(quantity_name + ' and ' + quantity_name2)

plt.show()
# -
import streamlit as st

