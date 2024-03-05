## Beginner Creating and View Data
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
})

# View the DataFrame
print(df)

## Intermediate data cleaning
# Handling missing values
df.fillna(value=0, inplace=True)

# Convert data types
df['Age'] = df['Age'].astype(int)

## Advanced Data Manipulation
# Grouping and aggregating
grouped = df.groupby('City').agg({'Age': ['mean', 'min', 'max']})

# Merging DataFrames
df2 = pd.DataFrame({
    'City': ['New York', 'Paris'],
    'Population': [8800000, 2141000]
})
merged_df = pd.merge(df, df2, on='City')

## Time Series Analysis
# Convert a column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Resample time series data
resampled_data = df.resample('M', on='Date').mean()

## Visualization 
# Requires matplotlib
df.plot(kind='bar', x='Name', y='Age')

