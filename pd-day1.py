import pandas as pd 
import numpy as np

# one dimensional data, in pandas, this is called a Series
# a series is a one dimensional array with labels (index)

grades = pd.Series([90, 80, 70, 60], index=['Alice', 'Bob', 'Charlie', 'David'])


# Accessing data in a series using labels
print(f"Alice Scored: {grades['Alice']}")
print(f"Charlie Scored: {grades['Charlie']}")
print(f"Bob Scored: {grades['Bob']}")
print(f"David Scored: {grades['David']}")


# dictionaries

students_data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [20, 21, 22, 23],
    'grade': [90, 80, 70, 60],
    'city': ['Nakuru', 'Mombasa', 'Naivasha', 'Kisumu'],
    'salary': [50000, 60000, 70000, 80000]
}

df = pd.DataFrame(students_data)
print(df)