import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)

# Define the number of samples
n_samples = 100

# Define the data
brands = ['Ford', 'Toyota', 'BMW', 'Honda', 'Chevrolet', 'Nissan', 'Hyundai', 'Kia', 'Mazda', 'Tesla']
body_styles = ['SUV', 'Sedan', 'Coupe', 'Hatchback', 'Convertible', 'Truck', 'Van']
years = np.random.randint(2015, 2022, n_samples)
mileages = np.random.randint(5000, 50000, n_samples)
prices = np.random.randint(15000, 40000, n_samples)

# Create the DataFrame
df = pd.DataFrame({
    'Brand': np.random.choice(brands, n_samples),
    'Price': prices,
    'Body_Style': np.random.choice(body_styles, n_samples),
    'Mileage': mileages,
    'Year': years
})

# Display the first few rows of the DataFrame
#print(df.head())

# Define the file path
file_path = './data/car_sales.csv'

# Append data to the file, without header if file exists
df.to_csv(file_path, mode='a', header=not file_path, index=False)

print("Data appended successfully to:", file_path)