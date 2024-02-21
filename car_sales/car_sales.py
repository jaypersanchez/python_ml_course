import pandas as pd

# Load dataset
df = pd.read_csv('car_sales.csv')
#Basic data inspection
# Display the first few rows
print(df.head())

# Summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())
