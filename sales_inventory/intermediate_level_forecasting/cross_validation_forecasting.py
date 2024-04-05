'''
This intermediate level while keeping the context of forecasting and data analytics, we can integrate more sophisticated data manipulation techniques, introduce cross-validation for time-series data, and implement a basic machine learning model for forecasting. This approach will give learners exposure to predictive modeling alongside the previously covered descriptive analytics.
Learning Value
Time Series Cross-Validation: Learners will understand how to properly validate models on time-series data.
Predictive Modeling: Introduces a simple machine learning model (Linear Regression) applied to time-series forecasting.
Feature Engineering: Demonstrates how to enrich models with time features.
Model Evaluation: Covers the basics of evaluating model performance using metrics like MAE (Mean Absolute Error) and MSE (Mean Squared Error).
This intermediate level exploration combines both forecasting and machine learning, giving learners practical skills in handling time-series data, a crucial aspect of many real-world data analytics scenarios.
'''
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

def load_and_prepare_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'])
    return df

def main():
    sales_data = load_and_prepare_data('../data/sales_records_data.json')
    
    # Ensure Purchase_Date is used for aggregation
    sales_data['YearMonth'] = sales_data['Purchase_Date'].dt.to_period('M')
    monthly_sales = sales_data.groupby(['YearMonth', 'Item_ID']).agg(Total_Quantity=('Quantity_Purchased', 'sum')).reset_index()
    monthly_sales['Year'] = monthly_sales['YearMonth'].dt.year
    monthly_sales['Month'] = monthly_sales['YearMonth'].dt.month
    
    # Prepare features and target variable
    X = monthly_sales[['Year', 'Month', 'Item_ID']]
    y = monthly_sales['Total_Quantity']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions
    predictions = model.predict(X_test)
    
    # Evaluate model
    print('MAE:', mean_absolute_error(y_test, predictions))
    print('MSE:', mean_squared_error(y_test, predictions))
    
    # Since we can't plot this directly due to grouping, this step is omitted
    
if __name__ == "__main__":
    main()
