import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('car_sales.csv')

sns.countplot(x='Body_Style', data=df)
plt.title('Sales by Body Style')
plt.xlabel('Body Style')
plt.ylabel('Number of Cars Sold')
plt.show()

