# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
csv_list = []

for i in range(9):
    csv_list.append(pd.read_csv("../album_data_23/" + str(2015+i) + "_23countries_album.csv"))

# %%
csv_list

# %%
csv_list[0]

# %%
df = pd.concat(csv_list)

# %%
df


# %%
df = df.drop(0)

# %%
df

# %%
df['Date'] = pd.to_datetime(df['기간'], format='%Y-%m')

# %%
df

# %%

# Example mapping dictionaries
country_to_english = {
    "네덜란드": "Netherlands",
    "독일": "Germany",
    "러시아": "Russia",
    "스페인": "Spain",
    "영국": "UK",
    "이탈리아": "Italy",
    "프랑스": "France",
    "베트남": "Vietnam",
    "싱가포르": "Singapore",
    "일본": "Japan",
    "중국": "China",
    "홍콩": "Hong Kong",
    "대만": "Taiwan",
    "사우디아라비아": "Saudi Arabia",
    "인도": "India",
    "인도네시아": "Indonesia",
    "태국": "Thailand",
    "호주": "Australia",
    "멕시코": "Mexico",
    "미국": "USA",
    "캐나다": "Canada",
    "브라질": "Brazil",
    "아르헨티나": "Argentina"
}

country_to_iso = {
    "Netherlands": "NL",
    "Germany": "DE",
    "Russia": "RU",
    "Spain": "ES",
    "UK": "GB",
    "Italy": "IT",
    "France": "FR",
    "Vietnam": "VN",
    "Singapore": "SG",
    "Japan": "JP",
    "China": "CN",
    "Hong Kong": "HK",
    "Taiwan": "TW",
    "Saudi Arabia": "SA",
    "India": "IN",
    "Indonesia": "ID",
    "Thailand": "TH",
    "Australia": "AU",
    "Mexico": "MX",
    "USA": "US",
    "Canada": "CA",
    "Brazil": "BR",
    "Argentina": "AR"
}

continent_group = {
    "Netherlands": "Europe",
    "Germany": "Europe",
    "Russia": "Europe",
    "Spain": "Europe",
    "UK": "Europe",
    "Italy": "Europe",
    "France": "Europe",
    "Vietnam": "East Asia",
    "Singapore": "East Asia",
    "Japan": "East Asia",
    "China": "East Asia",
    "Hong Kong": "East Asia",
    "Taiwan": "East Asia",
    "Saudi Arabia": "S Asia & Oceania",
    "India": "S Asia & Oceania",
    "Indonesia": "S Asia & Oceania",
    "Thailand": "S Asia & Oceania",
    "Australia": "S Asia & Oceania",
    "Mexico": "North America",
    "USA": "North America",
    "Canada": "North America",
    "Brazil": "South America",
    "Argentina": "South America"
}

# Goal 1: Change country name to English
df['Country'] = df['국가'].map(country_to_english)

# Goal 2: Initialize another column with ISO 3166 2-letter country code
df['ISO_Code'] = df['Country'].map(country_to_iso)

# Goal 3: Another column with each country's continent group
df['Continent'] = df['Country'].map(continent_group)

# Display the DataFrame
df


# %%
df = df.rename(columns={'수출 금액': 'Export', '수입 금액': 'Import', '무역수지': 'Balance'})
df


# %%
df_reconstructed = df.loc[:, ['Date', 'Country', 'ISO_Code', 'Continent', 'Export', 'Import', 'Balance']]
df_reconstructed

# %%
# Group by Date and Continent, then sum up Exports, Imports, and Balance
continent_summary = df.groupby(['Date', 'Continent']).agg({
    'Export': 'sum',
    'Import': 'sum',
    'Balance': 'sum'
}).reset_index()

# Pivot the table for easier plotting
pivot_df = continent_summary.pivot(index='Date', columns='Continent', values='Export')

# Plotting
pivot_df.plot(figsize=(14, 8), marker='o')
plt.title('Growth of Music Record Exports by Continent')
plt.xlabel('Date')
plt.ylabel('Total Export Value (1000 USD)')
plt.legend(title='Continent', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to make room for the legend
plt.show()

# %%
df_japan = df_reconstructed[df_reconstructed['Country'] == 'Japan']
df_japan.plot(x='Date', y='Export', kind='line', figsize=(10, 6))
plt.title('Export Value of Music Records in Japan')
plt.xlabel('Date')
plt.ylabel('Export Value (1000 USD)')
plt.grid(True)
plt.show()


# %%
df_taiwan = df_reconstructed[df_reconstructed['Country'] == 'Taiwan']
#draw more smooth graph
df_taiwan.plot(x='Date', y='Export', kind='line', figsize=(10, 6), marker='o')
plt.title('Export Value of Music Records in Taiwan')
plt.xlabel('Date')
plt.ylabel('Export Value (1000 USD)')
plt.grid(True)
plt.show()

# %%
df_japan[(df_japan['Date'].dt.year >= 2020) & (df_japan['Date'].dt.year <= 2023)]


# %%
df_taiwan[(df_taiwan['Date'].dt.year >= 2020) & (df_taiwan['Date'].dt.year <= 2023)]

# %%
# Filter the data for the years 2020-2023 and the specified regions
filtered_df = df_reconstructed[(df_reconstructed['Date'].dt.year >= 2020) & (df_reconstructed['Date'].dt.year <= 2023)]
filtered_df = filtered_df[(filtered_df['Continent'] == 'East Asia') | (filtered_df['Continent'] == 'S Asia & Oceania')]

# Group the data by country and calculate the sum of exports
grouped_df = filtered_df.groupby('Country')['Export'].sum().reset_index()

# Plotting the pie chart
plt.figure(figsize=(10, 6))
plt.pie(grouped_df['Export'], labels=grouped_df['Country'], autopct='%1.1f%%')
plt.title('Export Share of Music Records in East Asia and S Asia & Oceania (2020-2023)')
plt.show()


# %%
# Filter the data for the years 2020-2023 and the specified regions
filtered_df = df_reconstructed[(df_reconstructed['Date'].dt.year >= 2020) & (df_reconstructed['Date'].dt.year <= 2023)]
filtered_df = filtered_df[(filtered_df['Continent'] == 'Europe') | (filtered_df['Continent'] == 'North America')]

# Group the data by country and calculate the sum of exports
grouped_df = filtered_df.groupby('Country')['Export'].sum().reset_index()

# Plotting the pie chart
plt.figure(figsize=(10, 6))
plt.pie(grouped_df['Export'], labels=grouped_df['Country'], autopct='%1.1f%%')
plt.title('Export Share of Music Records in Europe and North America (2020-2023)')
plt.show()


# %%
# Filter the data for the years 2020-2023
filtered_df = df_reconstructed[(df_reconstructed['Date'].dt.year >= 2020) & (df_reconstructed['Date'].dt.year <= 2023)]

# Group the data by continent and calculate the sum of exports
grouped_df = filtered_df.groupby('Continent')['Export'].sum().reset_index()

# Plotting the pie chart
plt.figure(figsize=(10, 6))
plt.pie(grouped_df['Export'], labels=grouped_df['Continent'], autopct='%1.1f%%')
plt.title('Export Share of Music Records by Continent (2020-2023)')
plt.show()


# %%
# Filter the data for Japan and the years 2021-2023
df_japan_filtered = df_japan[(df_japan['Date'].dt.year >= 2021) & (df_japan['Date'].dt.year <= 2023)]

# Set the figure size
plt.figure(figsize=(10, 6))

# Plot the monthly sales using seaborn
sns.lineplot(data=df_japan_filtered, x='Date', y='Export')

# Set the title and labels
plt.title('Monthly Sales in Japan (2021-2023)')
plt.xlabel('Date')
plt.ylabel('Export Value (1000 USD)')

# Rotate the x-axis labels for better visibility
plt.xticks(rotation=45)

# Show the plot
plt.show()


# %%
# Filter the data for Japan, Taiwan, and the USA and the years 2020-2023
filtered_df = df_reconstructed[(df_reconstructed['Country'].isin(['Japan', 'Taiwan', 'USA'])) & (df_reconstructed['Date'].dt.year >= 2020) & (df_reconstructed['Date'].dt.year <= 2023)]

# Pivot the data to have countries as columns and export values as values
pivot_df = filtered_df.pivot(index='Date', columns='Country', values='Export')

# Calculate the correlation matrix
correlation_matrix = pivot_df.corr()

# Display the correlation matrix
correlation_matrix


# %%
sns.heatmap(correlation_matrix, annot = True, cmap = 'viridis')

# %%



