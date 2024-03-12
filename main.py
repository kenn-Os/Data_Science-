import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

# load dataset
df = pd.read_csv('PROJECT/covid.csv')

# show the first three rows
print(df.head(3))
print('\n')

# get the number of rows and columns
print(df.shape)
print('\n')

# checking for inconsistent values
print(df.isnull().values.any())
print('\n')

# remove / cleanse rows with null and nan values
df.dropna(subset=['dateRep', 'year', 'cases', 'deaths', 'countriesAndTerritories', 'popData2019', 'continentExp'], inplace=True)

# rename column names that we need
df.rename(columns={
    'dateRep': 'Date',
    'year': 'Year',
    'cases': 'Cases',
    'deaths': 'Deaths',
    'countriesAndTerritories': 'Countries',
    'popData2019': 'Population',
    'continentExp': 'Continent'
}, inplace=True)

# converting the date to pandas format
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# creating a list of important column
columns = ['Date', 'Year', 'Cases', 'Deaths', 'Countries', 'Population', 'Continent']

# show the first 3 rows of our prepered data
print(df[columns].head(3))
print('\n')

# show the last 3
print(df[columns].tail(3))
print('\n')

# the shape of the cleansed data
print(df[columns].shape)
print('\n')

# group / see the cummulative confirmed cases and deaths by country
df2 = df[['Countries', 'Cases', 'Deaths']].groupby('Countries').sum().reset_index()
# df2 = df[columns].groupby('Countries')[['Cases', 'Deaths']].sum().reset_index()
print(df2)
print('\n')

# group by countries and date
df3 = df[['Countries', 'Date', 'Cases', 'Deaths']].groupby(['Countries', 'Date']).sum().reset_index()
print(df3)
print('\n')

# display cases that are larger than 100
df4 = df3[df3['Cases'] > 100]
print(df4)
print('\n')

# get the continent and total cases
df5 = df[['Continent', 'Cases']].groupby('Continent').sum().reset_index()
print(df5)
print('\n')

# get how many countries are in this file
countries = df3['Countries'].unique()
print(len(countries))
# print(df3[df3['Countries'] == countries[1]])
# print(df3['Countries'])
print('\n')



# data visualization using matplotlib
# seeing the trend of virus for each country with respect to date
for i in range(len(countries)):
    c = df3[df3['Countries'] == countries[i]].reset_index()
    plt.scatter(np.arange(len(c)), c['Cases'], color='blue', label='Confirmed')
    plt.scatter(np.arange(len(c)), c['Deaths'], color='red', label='Deaths')
    plt.title(countries[i])
    plt.xlabel('Days since the first suspect')
    plt.ylabel('Number of Cases and Deaths')
    plt.legend()
    plt.show()

c = df3.groupby('Date')[['Cases', 'Deaths']].sum().reset_index()
plt.scatter(np.arange(len(c)), c['Cases'], color='blue', label='Confirmed')
plt.scatter(np.arange(len(c)), c['Deaths'], color='red', label='Deaths')
plt.title('World Analysis')
plt.xlabel('Days since the first suspect')
plt.ylabel('Number of Cases and Deaths')
plt.legend()
plt.show()


