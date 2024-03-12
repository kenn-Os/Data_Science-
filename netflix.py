import pandas as pd 
import numpy as np

# Load Dataset
df = pd.read_csv('PROJECT/netflix.csv')

# show the top 5 records
print(df.head(5))
print('\n')

# Show the bottom 5 records 
print(df.tail(5))
print('\n')

# Show the number of rows and columns
print(df.shape)
print('\n')

# Show the number of total values in the dataset
print(df.size)
print('\n')

# Show each column name
print(df.columns)
print('\n')

# Show the data type of each column
print(df.dtypes)
print('\n')

# What is the show Id and who is the director
print(df[['show_id', 'director']])
print('\n')

# What is the show Id and who is the director first 5
print(df[['show_id', 'director']].head(5))
print('\n')

# Show all movies that were released in the year 2010
print(df[df['release_year'] == 2010])
print('\n')

# Show only the title of TV Show released in Argentina
print(df[(df['type'] == 'TV Show') & (df['country'] == 'Argentina')])
print('\n')

# Show top 10 directors for movies or tv shows
print(df[['director']].head(10))
print('\n')

# show all the records were type is comedies or country is argentina
print(df[(df['type'] == 'Comedies') | (df['country'] == 'Argentina')])

# in how many movie/show Júlia Gomes was cast
