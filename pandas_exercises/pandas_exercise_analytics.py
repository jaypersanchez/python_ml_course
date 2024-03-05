import pandas as pd
import matplotlib.pyplot as plt

## Beginner Level Data Load
# Assuming 'data.csv' contains your dataset
df = pd.read_csv('data/car_sales.csv')
print(df.head())

## Intermediate Level Data Cleaning
# Since your data may not have missing values or duplicates based on the example, this step could be theoretical.
# Convert 'Year' to categorical as it might be treated as a feature rather than a numerical value.
df['Year'] = df['Year'].astype('category')

## Intermediate-Advanced Manipulation
# Group by 'Brand' and aggregate by average 'Price'
grouped = df.groupby('Brand').agg({'Price': 'mean'})

print(grouped)

## Advanced Data Analysis
# The merging and rolling window calculations might not directly apply to your dataset without further context or additional datasets.

## Advanced Time Series Analysis
# Your dataset doesn't include a datetime column, but if 'Year' was used in a time series context:
df.set_index('Year', inplace=True)
# This theoretical step assumes temporal analysis which isn't directly applicable with just the 'Year' field.
print(df)

# Display result for user
# Calculate average price per year
#average_price_per_year = df.groupby('Year')['Price'].mean()

# Plotting
grouped.plot(kind='bar')
plt.title('Average Car Price per Year')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.show()