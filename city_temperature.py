import pandas as pd

# Sample data - temperatures for City A and City B
temps_city_a = [23, 25, 22, 26, 25, 24, 23]  # Replace with actual temperature data
temps_city_b = [31, 32, 31, 30, 29, 30, 31]  # Replace with actual temperature data

# Creating the DataFrame
temps_df = pd.DataFrame({'City A': temps_city_a, 'City B': temps_city_b})

# Adding a new column for the day of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temps_df['Day'] = days

# Reordering columns
temps_df = temps_df[['Day', 'City A', 'City B']]

# Display the DataFrame
print(temps_df)
