import pandas as pd
import numpy as np

# Task 1.2: Create a Series from a list
data = [4, 7, -5, 3]
series = pd.Series(data)
print("Series without custom index:\n", series)

# Task 1.3: Assign labels to the index
index_labels = ['d', 'b', 'a', 'c']
series.index = index_labels
print("\nSeries with custom index:\n", series)

# Access element at index 'b'
print("Element at index 'b':", series['b'])

# Slice the Series from 'b' to 'c'
print("\nSeries from 'b' to 'c':\n", series['b':'c'])

# Multiply Series by 2 will require numpy
print("Series * 2:\n", series * 2)

# Exponential of Series
print("\nExponential of Series:\n", np.exp(series))

# Create a Series with missing data
data_with_missing = [4, np.nan, -5, None]
series_missing = pd.Series(data_with_missing)
print("Series with missing data:\n", series_missing)

# Find missing and non-missing values
print("\nMissing values:\n", series_missing.isnull())
print("\nNon-missing values:\n", series_missing.notnull())
