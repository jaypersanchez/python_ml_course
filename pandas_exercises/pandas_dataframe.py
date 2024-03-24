import pandas as pd

# Task 1 Create DataFrame
data = {
    'Name': ['Anna', 'Bob', 'Catherine', 'David', 'Emily'],
    'Age': [28, 34, 29, 42, 21],
    'City': ['New York', 'Paris', 'Berlin', 'London', 'Tokyo']
}
df = pd.DataFrame(data)
# Display DataFrame
print(df)

# Task 2 Access 'Name' column
print(df['Name'])
# Access the first row
print(df.iloc[0])
# Access the age of Catherine
print(df.loc[df['Name'] == 'Catherine', 'Age'].item())

# Task 3 Add 'Salary' column
df['Salary'] = [50000, 60000, 52000, 45000, 58000]
print("\nDataFrame with 'Salary' column:\n", df)

# Delete 'City' column
df.drop('City', axis=1, inplace=True)
print("\nDataFrame without 'City' column:\n", df)

# Task 4 - Filter rows where Age > 30
print("\nRows where Age > 30:\n", df[df['Age'] > 30])

# Calculate average age
print("\nAverage Age:", df['Age'].mean())
