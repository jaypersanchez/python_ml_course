"""
Imagine you have a toy rocket that you're trying to fly straight up into the sky. 
The "R-squared value" is like a game score that tells us how well we aimed our rocket to fly 
straight up. If we get a score of 1 (or 100%), it means we did a perfect job, 
and our rocket flew exactly where we wanted it to go.

Now, your score came out to be -0.13, which is like saying our rocket didn't really go up; instead, 
it kind of went in the wrong direction a little bit. In grown-up words, 
it means the information we used to predict how many toys (or "sales volume") 
we could sell based on their price tags and sale stickers didn't really help us make a good guess. 

Instead of helping us guess better, it was a bit like guessing without looking.
So, just like when playing a game, if our score isn't good, 
we try again or try using different toys or rules to get a better score next time. 

In our case, we might try looking at other things about the toys that might help us guess better 
how many we can sell, like what kind of toys they are or if they're more popular at certain 
times of the year.
"""
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Function to load data from a JSON file
def load_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return pd.DataFrame(json.load(file))

# Load sales inventory data
sales_inventory_data = load_data_from_json('./data/sales_inventory_data.json')

# Assuming you're interested in predicting Sales_Volume based on Price and Discount_Rate from sales_inventory_data
X = sales_inventory_data[['Price', 'Discount_Rate']]
y = sales_inventory_data['Sales_Volume']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
r_squared = r2_score(y_test, y_pred)
print(f"R-squared value: {r_squared:.2f}")

# Visualize the results
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
plt.xlabel('Actual Sales Volume')
plt.ylabel('Predicted Sales Volume')
plt.title('Actual vs Predicted Sales Volume')
plt.show()
