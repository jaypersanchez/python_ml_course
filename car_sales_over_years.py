import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('car_sales.csv')

df.groupby('Year')['Brand'].count().plot(kind='bar')
plt.title('Car Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Cars Sold')
plt.show()



