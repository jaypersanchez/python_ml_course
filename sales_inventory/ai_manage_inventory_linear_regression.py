"""
To illustrate regression analysis based on the sales inventory and sales records data, 
we'll first need to establish a relationship we're interested in analyzing. 
A common approach is to model how sales volume (dependent variable) changes in relation to 
other factors such as price, discount rate, or time (independent variables).

In this example, let's assume we're interested in understanding how the discount rate affects 
sales volume for items. We'll perform a simple linear regression analysis to explore this relationship.
This requires calculating the average sales volume for each discount rate across all items, 
then fitting a regression model to this data.
"""

import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def load_data_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def merge_sales_and_inventory(sales_records, inventory_data):
    return pd.merge(sales_records, inventory_data[['Item_ID', 'Discount_Rate']], on='Item_ID')

def calculate_average_sales_by_discount(merged_data):
    return merged_data.groupby('Discount_Rate').agg({'Quantity_Purchased':'mean'}).reset_index()

def perform_linear_regression(avg_sales_by_discount):
    return stats.linregress(avg_sales_by_discount['Discount_Rate'], avg_sales_by_discount['Quantity_Purchased'])

def visualize_regression(avg_sales_by_discount, slope, intercept):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Discount_Rate', y='Quantity_Purchased', data=avg_sales_by_discount, color='blue', label='Average Sales')
    plt.plot(avg_sales_by_discount['Discount_Rate'], intercept + slope * avg_sales_by_discount['Discount_Rate'], 'r', label='Fitted Line')
    plt.title('Effect of Discount Rate on Average Sales Volume')
    plt.xlabel('Discount Rate')
    plt.ylabel('Average Sales Volume')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Load data from JSON files
    sales_inventory_data = pd.DataFrame(load_data_from_json('./data/sales_inventory_data.json'))
    sales_records_data = pd.DataFrame(load_data_from_json('./data/sales_records_data.json'))

    # Merge sales records with inventory data
    merged_data = merge_sales_and_inventory(sales_records_data, sales_inventory_data)

    # Calculate average sales volume by discount rate
    avg_sales_by_discount = calculate_average_sales_by_discount(merged_data)

    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = perform_linear_regression(avg_sales_by_discount)
    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")
    print(f"R-squared: {r_value**2}")
    print(f"P-value: {p_value}")

    # Visualize the regression analysis
    visualize_regression(avg_sales_by_discount, slope, intercept)
