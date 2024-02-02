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

ori_df = pd.read_csv('../original_data/KAIST_kpopradar_tiktok_video_creation_20230930.csv')
df = ori_df.copy()
ori_df

extract_pattern = '(^.*)\s?[\[\-]'
df['extracted1_song'] = df['song'].str.extract(extract_pattern, expand = False)
df['extracted1_song'].fillna(df['song'], inplace=True) ##NaN 채우기
df

extract_bar_pattern = '(^.*)\s?[\-]'
df['extracted2_song'] = df['extracted1_song'].str.extract(extract_pattern, expand = False)
df['extracted2_song'].fillna(df['extracted1_song'], inplace=True) ##NaN 채우기
df

test_artist_name = "BLACKPINK"
test_song_name = "DDU"

test_before = ori_df[(ori_df['artist_name'].str.contains(test_artist_name)) & (ori_df['song'].str.contains(test_song_name))]
test_before

test_before['song'].unique()

## 1. 대괄호, 작대기를 날린다
    ## 1-1. 그러면 DDU-DU가 필터링된다 => 폐기
## 2. 한글 (영어) 형태를 regex로 capture해서 뚜두뚜두 or DDU-DU DDU-DU 포함 => DDU-DU DDU-DU 로 바꾼다.
pattern_ko_en = '[\u3131-\uD79D\s]+ \([A-Za-z\s]+\)'  # 한국어 (영어)

test_after = df[(df['artist_name'].str.contains(test_artist_name)) & (df['song'].str.contains(test_song_name))]
test_after
## 데이터 Row 개수 보존

test_after['extracted1_song'].unique()

test_after['extracted2_song'].unique()


