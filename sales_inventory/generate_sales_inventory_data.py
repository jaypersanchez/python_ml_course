import json
import numpy as np
from datetime import datetime
import pandas as pd

def convert_np_arrays_to_lists(data):
    # This function remains unchanged; it's here for completeness
    if isinstance(data, dict):
        return {k: convert_np_arrays_to_lists(v) for k, v in data.items()}
    elif isinstance(data, np.ndarray):
        return data.tolist()
    return data

def restructure_data_for_json(data):
    # Convert the dictionary of lists into a list of dictionaries
    keys = data.keys()
    return [dict(zip(keys, record)) for record in zip(*data.values())]

def save_data_to_json(data, filename):
    # First, convert the data structure
    data = convert_np_arrays_to_lists(data)
    # Then, restructure data to the desired format
    structured_data = restructure_data_for_json(data)
    # Finally, save to a JSON file
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(structured_data, file, indent=4)

# Example usage with sales_inventory_data
sales_inventory_data = {
    'Item_ID': np.arange(1, 101),
    'Category': np.random.choice(['Electronics', 'Clothing', 'Groceries'], 100),
    'Price': np.random.uniform(5, 100, 100).round(2),
    'Discount_Rate': np.random.choice([0, 0.1, 0.2, 0.3], 100),
    'Sales_Volume': np.random.randint(10, 100, 100),
    'Stock_On_Hand': np.random.randint(0, 50, 100)
}

# Generate purchase dates as strings
start_date = datetime.now().date()
purchase_dates = pd.date_range(start=start_date, periods=150, freq='D')
purchase_dates_str = [date.strftime('%Y-%m-%d') for date in purchase_dates]

# Example usage with sales_records_data
sales_records_data = {
    'Item_ID': np.random.choice(sales_inventory_data['Item_ID'], 150, replace=True),
    'Quantity_Purchased': np.random.randint(1, 10, 150),
    'Purchase_Date': purchase_dates_str,
}

# Save to JSON files
save_data_to_json(sales_inventory_data, './data/sales_inventory_data.json')
save_data_to_json(sales_records_data, './data/sales_records_data.json')
