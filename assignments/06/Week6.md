# Week 6 Assignment

import pandas as pd

df = pd.read_csv(r'C:\Users\Joshua Christian\Desktop\Semester 3\DIS08\06_python_intro.ipynb\data\data\2022_circ.csv')

df.columns = df.columns.str.strip()

## Task 1: Get basic info about the DataFrame
print("Basic Info about DataFrame:")
print(df.info())

## Task 2: View the first few rows
print("\nFirst 5 rows of the DataFrame:")
print(df.head())

## Task 3: View the last few rows
print("\nLast 5 rows of the DataFrame:")
print(df.tail())

## Task 4: Get a statistical summary of the DataFrame
print("\nStatistical summary of the DataFrame:")
print(df.describe())

## Task 5: Get column names
print("\nColumn names:")
print(df.columns)

## Task 6: Get the first 10 rows
print("\nFirst 10 rows:")
print(df.head(10))

## Task 7: Get the last 10 rows
print("\nLast 10 rows:")
print(df.tail(10))

## Task 8: Get rows between row 30 and row 40
print("\nRows between 30 and 40 (inclusive):")
print(df.iloc[30:41])

## Task 9: Get a specific column (e.g., 'year')
## First, check if the 'year' column exists
if 'year' in df.columns:
    print("\nAccessing the 'year' column:")
    year_column = df['year']
    print(year_column)
    print("\nType of the 'year' column:")
    print(type(year_column))
else:
    print("\n'year' column not found!")

## Task 10: Using .loc() to access a row by label
print("\nUsing .loc() to access row 10 (by label):")
print(df.loc[10])

## Task 11: Using .iloc() to access a row by position
print("\nUsing .iloc() to access row 10 (by position):")
print(df.iloc[10])

## Task 12: Sort values by the 'year' column
## Check if 'year' column exists before sorting
if 'year' in df.columns:
    print("\nSorting values by the 'year' column:")
    df_sorted = df.sort_values(by='year')
    print(df_sorted)
else:
    print("\n'year' column not found for sorting!")
