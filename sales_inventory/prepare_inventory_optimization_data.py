import json
import pandas as pd

def load_json_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def merge_data(sales_inventory, sales_records, item_details):
    # Convert lists to DataFrames
    df_inventory = pd.DataFrame(sales_inventory)
    df_records = pd.DataFrame(sales_records)
    df_details = pd.DataFrame(item_details)
    
    # Calculate monthly demand from sales records
    df_records['Purchase_Date'] = pd.to_datetime(df_records['Purchase_Date'])
    monthly_demand = df_records.groupby([df_records['Item_ID'], df_records['Purchase_Date'].dt.to_period('M')])['Quantity_Purchased'].sum().reset_index()
    monthly_demand = monthly_demand.groupby('Item_ID')['Quantity_Purchased'].mean().reset_index()
    monthly_demand.columns = ['Item_ID', 'Monthly_Demand']
    
    # Merge all dataframes
    df_merged = pd.merge(df_inventory, monthly_demand, on="Item_ID", how="left")
    df_merged = pd.merge(df_merged, df_details, on="Item_ID", how="left")
    
    # Add placeholders for missing data (to be filled in manually or with another data source)
    df_merged['Holding_Cost'] = None  # Placeholder for holding cost
    df_merged['Order_Cost'] = None    # Placeholder for order cost
    df_merged['Lead_Time'] = None     # Placeholder for lead time
    
    return df_merged

if __name__ == "__main__":
    # Load data from JSON files
    sales_inventory_data = load_json_data('data/sales_inventory_data.json')
    sales_records_data = load_json_data('data/sales_records_data.json')
    item_details_data = load_json_data('data/item_details.json')
    
    # Merge data
    merged_data = merge_data(sales_inventory_data, sales_records_data, item_details_data)
    
    # Export merged data to a new JSON file
    merged_data.to_json('data/optimized_inventory_data.json', orient='records', date_format='iso')
    
    print("Merged data has been saved to 'optimized_inventory_data.json'.")
