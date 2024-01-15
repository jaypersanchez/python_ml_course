import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('car_sales.csv')

plt.hist(df['Price'], bins=10, color='blue')
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()
