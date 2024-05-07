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

import os
current_directory = os.getcwd()
print(current_directory) 

df=pd.read_csv('../original_data/KAIST_kpopradar_youtube_channel_20230930.csv')

df.head()

#checking for unique values
df['artist_name'].unique().shape

df.shape

# Description of the Data
df.describe().astype(int)

# +
# Get specified data for BLACKPINK artist_name, type conversion of 'date' column to datetime

BLACKPINK_df = df[df['artist_name'] == 'BLACKPINK'].sort_values('date')
BLACKPINK_df['date'] = pd.to_datetime(BLACKPINK_df['date'], format='%Y%m%d')
# -

BLACKPINK_df

from matplotlib.ticker import ScalarFormatter, MaxNLocator

# +
# Replace 'specified_date' with the date you want to compare against (in datetime format)
specified_date = pd.to_datetime('2022-01-01')

# Filter the DataFrame to get rows with date greater than specified_date
filtered_BLACKPINK_df = BLACKPINK_df[BLACKPINK_df['date'] > specified_date]

plt.figure(figsize = (15,8))
plt.plot(filtered_BLACKPINK_df['date'], filtered_BLACKPINK_df['subscriber_count'])

# Apply ScalarFormatter to the y-axis (subscriber_count)
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=False))
plt.ticklabel_format(style='plain', axis='y')  # Another way to disable scientific notation

plt.title('BLACKPINK YouTube Subscribers')
plt.xlabel('Date')
plt.ylabel('Subscriber Count')

plt.show()

# +
# Replace 'specified_date' with the date you want to compare against (in datetime format)
specified_date = pd.to_datetime('2018-01-01')

# Filter the DataFrame to get rows with date greater than specified_date
filtered_BLACKPINK_df = BLACKPINK_df[BLACKPINK_df['date'] > specified_date]

plt.figure(figsize = (15,8))
plt.plot(filtered_BLACKPINK_df['date'], filtered_BLACKPINK_df['subscriber_count'])

# Apply ScalarFormatter to the y-axis (subscriber_count)
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=False))
plt.ticklabel_format(style='plain', axis='y')  # Another way to disable scientific notation

plt.title('BLACKPINK YouTube Subscribers')
plt.xlabel('Date')
plt.ylabel('Subscriber Count')

plt.show()

# +
#Goal: How to get monthly-splitted plot?

# +
# Replace 'specified_date' with the date you want to compare against (in datetime format)
start_date = pd.to_datetime('2019-09-01') ### Change Here!
end_date = pd.to_datetime('2021-04-01')
quantity_name = 'subscriber_count' ### Type the column name of desired quantity!

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

plt.title('BLACKPINK Twitter' + ' ' + quantity_name)
plt.xlabel('Date')
plt.ylabel(quantity_name)

plt.show()
