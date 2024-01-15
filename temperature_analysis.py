import numpy as np

# Sample temperatures for a week in City A and City B
temps_city_a = np.array([23, 25, 22, 26, 25, 24, 23])
temps_city_b = np.array([31, 32, 31, 30, 29, 30, 31])

# Usage of mean, max, min. Calculating average temperature for each city
avg_temp_a = np.mean(temps_city_a)
avg_temp_b = np.mean(temps_city_b)

print(f"Average temperature in City A: {avg_temp_a} °C")
print(f"Average temperature in City B: {avg_temp_b} °C")

# Find the max and min temperatures for each city
max_temp_a = np.max(temps_city_a)
min_temp_a = np.min(temps_city_a)

print(f"Highest and lowest temperatures in City A: {max_temp_a} °C, {min_temp_a} °C")
