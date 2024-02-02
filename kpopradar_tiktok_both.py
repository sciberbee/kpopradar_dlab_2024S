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

df_tikf = pd.read_csv('../original_data/KAIST_kpopradar_tiktok_followers_20230930.csv')
df_tikv = pd.read_csv('../original_data/KAIST_kpopradar_tiktok_video_creation_20230930.csv')

df_tikf

df_tikv

bp_followers = df_tikf[df_tikf['artist_name'].str.contains("BLACKPINK")]
bp_followers

bts_followers = df_tikf[df_tikf['artist_name'].str.contains("방탄소년단")]  #너는 왜 또 방탄소년단이야??
bts_followers

bp_videos = df_tikv[df_tikv['artist_name'].str.contains("BLACKPINK")]
bp_videos

bts_videos = df_tikv[df_tikv['artist_name'].str.contains("BTS")]
bts_videos

bp_followers['artist_name'].unique()

bp_videos['artist_name'].unique()

bts_videos['artist_name'].unique()

bp_videos['artist_name'] = bp_videos['artist_name'].replace(bp_videos['artist_name'].unique(), 'BLACKPINK')

bp_videos['artist_name'].unique()

bp_videos['date'] = pd.to_datetime(bp_videos['date'], format='%Y%m%d')
bp_videos

bp_videos_datesum = bp_videos.groupby('date')['videos'].sum().reset_index()
bp_videos_datesum

bp_followers['date'] = pd.to_datetime(bp_followers['date'], format='%Y%m%d')
bp_followers

bp_followers_datesum = bp_followers.groupby('date')['followers'].sum().reset_index()
bp_followers_datesum

from matplotlib.ticker import ScalarFormatter, MaxNLocator
import matplotlib.dates as mdates

# +
# Replace 'specified_date' with the date you want to compare against (in datetime format)
start_date = pd.to_datetime('2022-01-01') ### Change Here!
end_date = pd.to_datetime('2023-12-01')
quantity_name = 'followers' ### Type the column name of desired quantity!
quantity_name2 = 'videos'

# Filter the DataFrame to get rows with date greater than specified_date
filtered_bp_followers_datesum = bp_followers_datesum[(bp_followers_datesum['date'] > start_date) & (bp_followers_datesum['date'] < end_date)]
filtered_bp_videos_datesum = bp_videos_datesum[(bp_videos_datesum['date'] > start_date) & (bp_videos_datesum['date'] < end_date)]

plt.figure(figsize = (15,8))
plt.plot(filtered_bp_followers_datesum['date'], filtered_bp_followers_datesum[quantity_name], label = quantity_name, color = 'skyblue')
plt.plot(filtered_bp_videos_datesum['date'], filtered_bp_videos_datesum[quantity_name2], label = quantity_name2, color = 'red')
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

plt.title('BLACKPINK TikTok followers and video counts')
plt.xlabel('Date')
plt.ylabel(quantity_name + ' and ' + quantity_name2)

plt.show()

# +
# Replace 'specified_date' with the date you want to compare against (in datetime format)
start_date = pd.to_datetime('2023-03-01') ### Change Here!
end_date = pd.to_datetime('2023-04-01')
quantity_name = 'followers' ### Type the column name of desired quantity!
quantity_name2 = 'videos'

# Filter the DataFrame to get rows with date greater than specified_date
filtered_bp_followers_datesum = bp_followers_datesum[(bp_followers_datesum['date'] > start_date) & (bp_followers_datesum['date'] < end_date)]
filtered_bp_videos_datesum = bp_videos_datesum[(bp_videos_datesum['date'] > start_date) & (bp_videos_datesum['date'] < end_date)]

plt.figure(figsize = (15,8))
plt.plot(filtered_bp_followers_datesum['date'], filtered_bp_followers_datesum[quantity_name], label = quantity_name, color = 'skyblue')
plt.plot(filtered_bp_videos_datesum['date'], filtered_bp_videos_datesum[quantity_name2], label = quantity_name2, color = 'red')
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

plt.title('BLACKPINK TikTok followers and video counts')
plt.xlabel('Date')
plt.ylabel(quantity_name + ' and ' + quantity_name2)

plt.show()
# -

filtered_bp_videos_datesum


