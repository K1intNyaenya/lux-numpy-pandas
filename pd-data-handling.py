import pandas as pd
import numpy as np

df = pd.read_csv('auto-mpg.csv')

# viewing the first few rows of the DataFrame
# print(df.head())

# using the info() method to get a concise summary of the DataFrame
# print(df.info())

# using the describe() method to get summary statistics of the DataFrame
# print(df.describe())

# using the value_counts() method to get the count of unique values in a column
# print(df['cylinders'].value_counts())

# selecting a specific column from the DataFrame
cylinders = df['cylinders']
# print(cylinders)

# selecting rows
# print(df.iloc[0])  # first row
# print(df.iloc[1:4])  # rows 1 to 3
# print(df.iloc[1:4])  # rows 1 to 3
# print(df.iloc[1:3])  # rows 1 to 2


# selecting rows using label-based indexing
# print(df.loc[0])  # first row
# print(df.loc[1:4])  # rows 1 to 4 (inclusive)
# print(df.loc[1:4])  # rows 1 to 4 (inclusive)
# print(df.loc[1:3])  # rows 1 to 3 (inclusive)


## Logical operators in pandas
# selecting rows based on a condition
# print(df[df['mpg'] > 18]) # rows where mpg is greater than 18

#print(df[(df['mpg'] > 18) & (df['cylinders'] == 4)]) # rows where mpg is greater than 18 and cylinders is equal to 4

#print(df[(df['mpg'] > 18) | (df['cylinders'] == 4)]) # rows where mpg is greater than 18 or cylinders is equal to 4

# using contains
# print(df[df['car name'].str.contains('ford')]) # rows where car name contains 'ford'

# checking total number of chevrolet cars in the dataset
# print(df[df['car name'].str.contains('chevrolet')].shape[0])

# Filter the dataset to show vehicles with hp greater than 50 and print out the car names


# sorting by horsepower
print(df.sort_values('horsepower', ascending=True)) # sort by horsepower in ascending order