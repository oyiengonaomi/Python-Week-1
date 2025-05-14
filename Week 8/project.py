import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px  # For choropleth maps

# 1. Data Collection
# Load the dataset
data_path = 'owid-covid-data.csv' 
try:
    df = pd.read_csv(data_path)
except FileNotFoundError:
    print(f"Error: File not found at {data_path}. Please download the dataset and ensure the path is correct.")
    #  To make the rest of the code runnable,  exit if file not found.
    exit()

# 2. Data Loading & Exploration
# Check columns
print("Columns in the dataset:")
print(df.columns)

# Preview rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Identify missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# 3. Data Cleaning
# Filter countries of interest
countries_of_interest = ['Kenya', 'USA', 'India']
df_filtered = df[df['location'].isin(countries_of_interest)].copy()  # Creating a copy to avoid SettingWithCopyWarning

# Drop rows with missing dates or critical values.  
df_filtered.dropna(subset=['date', 'total_cases'], inplace=True)

# Convert date column to datetime
df_filtered['date'] = pd.to_datetime(df_filtered['date'])

# Handle missing numeric values.  Important to do this *after* filtering
numeric_cols = ['total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_vaccinations', 'people_vaccinated']
for col in numeric_cols:
    if col in df_filtered.columns: # Check if the column exists
        df_filtered[col].fillna(0, inplace=True)  #  simple strategy

# 4. Exploratory Data Analysis (EDA)
# Plot total cases over time for selected countries
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.show()

# Plot total deaths over time
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)
plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.show()

# Compare daily new cases between countries
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['new_cases'], label=country)
plt.title('Daily New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.show()

# Calculate the death rate: total_deaths / total_cases
df_filtered['death_rate'] = df_filtered['total_deaths'] / df_filtered['total_cases']

# 5. Visualizing Vaccination Progress
# Plot cumulative vaccinations over time for selected countries
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
plt.title('Cumulative COVID-19 Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.show()

# Compare % vaccinated population (requires people_vaccinated and population data)
if 'people_vaccinated' in df_filtered.columns and 'population' in df_filtered.columns:
    df_filtered['vaccination_rate'] = (df_filtered['people_vaccinated'] / df_filtered['population']) * 100
    plt.figure(figsize=(10, 6))
    for country in countries_of_interest:
        country_data = df_filtered[df_filtered['location'] == country]
        plt.plot(country_data['date'], country_data['vaccination_rate'], label=country)
    plt.title('Percentage of Population Vaccinated Over Time')
    plt.xlabel('Date')
    plt.ylabel('Vaccination Rate (%)')
    plt.legend()
    plt.show()
else:
    print("Warning:  Cannot calculate vaccination rate.  'people_vaccinated' or 'population' columns are missing.")

# 6. Build a Choropleth Map
# Preparing a dataframe with iso_code, total_cases for the latest date
latest_data = df[df['date'] == df['date'].max()]
latest_data = latest_data[['iso_code', 'total_cases', 'location']] #added location

# Plot a choropleth map showing case density
if 'iso_code' in latest_data.columns:
    fig = px.choropleth(latest_data,
                        locations="iso_code",
                        color="total_cases",
                        hover_name="location", #added location to hover
                        color_continuous_scale=px.colors.sequential.Plasma,
                        title="Total COVID-19 Cases by Country (Latest Date)",
                        projection='natural earth')  #  Consider using 'natural earth'
    fig.show()
else:
    print("Warning: Cannot plot choropleth map. 'iso_code' column is missing.")

# 7. Insights & Reporting
print("""
Insights:
* The USA has the highest total number of cases among the selected countries.
* India experienced a surge in cases around mid-2021.
* Kenya's case numbers are lower compared to the USA and India, but the trend is still upwards.
* Vaccination progress varies significantly between the selected countries.
""")
