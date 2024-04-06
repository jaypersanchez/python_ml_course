'''
To illustrate how polynomial regression can model non-linear relationships between price, discount rate, and sales volume.
To demonstrate data preprocessing steps, including merging datasets and creating polynomial features.
To fit a polynomial regression model and evaluate its performance.
'''
import pandas as pd
import numpy as np
import json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load JSON Data
def load_data_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# Merging Data
def merge_data(item_details, sales_inventory):
    df_details = pd.DataFrame(item_details)
    df_sales_inventory = pd.DataFrame(sales_inventory)
    merged_df = pd.merge(df_details, df_sales_inventory, on="Item_ID")
    return merged_df

# Polynomial Regression Function
def polynomial_regression(data, degree=2, features=['Price', 'Discount_Rate'], target='Sales_Volume'):
    # Prepare features and target variable
    X = data[features]
    y = data[target]

    # Generating polynomial features
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)

    # Splitting dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

    # Model fitting
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluation
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2}")

    # Visualization
    plt.scatter(y_test, y_pred)
    plt.xlabel('Actual Sales Volume')
    plt.ylabel('Predicted Sales Volume')
    plt.title('Actual vs. Predicted Sales Volume')
    plt.show()

    return model

# Main Function
if __name__ == "__main__":
    item_details = load_data_from_json('data/item_details.json')
    sales_inventory = load_data_from_json('data/sales_inventory_data.json')

    merged_data = merge_data(item_details, sales_inventory)

    # Perform polynomial regression with a degree of 2
    model = polynomial_regression(merged_data, degree=2)
