import pandas as pd
import numpy as np

# set random seed for reproducibility
np.random.seed(42)

# Generate 100 random items that are for sale
salesInventoryData = {
        'Item_ID': np.arange(1, 101),
        'Category': np.random.choice(['Electronics', 'Clothing', 'Groceries'], 100),
        'Price': np.random.uniform(5, 100, 100).round(2),
        'Discount_Rate': np.random.choice([0, 0.1, 0.2, 0.3], 100),
        'Sales_Volume': np.random.randint(10, 100, 100),
        'Stock_On_Hand': np.random.randint(0, 50, 100)
}

df_inventory = pd.DataFrame(salesInventoryData)

# Generate 150 random sales records based on the Item_ID from salesInventoryData
sales_records_data = {
    'Item_ID': np.random.choice(df_inventory['Item_ID'], 150, replace=True),  # Allow repetition of Item_ID
    'Quantity_Purchased': np.random.randint(1, 10, 150),
    'Purchase_Date': pd.date_range(start='2022-11-01', periods=150, freq='D').tolist()
}

salesInventoryDataClassified = {
    'Item_ID': np.arange(1, 101),
    'Category': np.random.choice(['Electronics', 'Clothing', 'Groceries'], 100),
    'Price': np.random.uniform(5, 100, 100).round(2),
    'Discount_Rate': np.random.choice([0, 0.1, 0.2, 0.3], 100),
    'Sales_Volume': np.random.randint(10, 100, 100),
    'Stock_On_Hand': np.random.randint(0, 50, 100),
    'Average_Monthly_Sales': np.random.randint(10, 100, 100),
    'Days_Until_Holiday': np.random.randint(1, 60, 100),
}


# Determine which item will run out before the holidays
#df['Will_Run_Out'] = ((df['Stock_On_Hand'] - df['Average_Monthly_Sales'] * (df['Days_Until_Holiday'] / 30)) < 0).astype(int)
#print(df.head())