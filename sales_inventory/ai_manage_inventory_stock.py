import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def calculate_average_monthly_sales(sales_records):
    sales_records['Purchase_Date'] = pd.to_datetime(sales_records['Purchase_Date'])
    monthly_sales = sales_records.groupby([sales_records['Purchase_Date'].dt.to_period('M'), 'Item_ID']).agg({'Quantity_Purchased': 'sum'}).reset_index()
    avg_monthly_sales = monthly_sales.groupby('Item_ID')['Quantity_Purchased'].mean().reset_index()
    avg_monthly_sales.columns = ['Item_ID', 'Avg_Monthly_Sales']
    return avg_monthly_sales

def estimate_stockout_probability(inventory_data, sales_data, months_ahead=3):
    # Merge average monthly sales with inventory data
    df_analysis = pd.merge(inventory_data, sales_data, on='Item_ID')
    # Calculate months until stockout
    df_analysis['Months_Until_Stockout'] = df_analysis['Stock_On_Hand'] / df_analysis['Avg_Monthly_Sales']
    # Determine stockout probability in the next few months
    df_analysis['Probability_Stockout_3Months'] = df_analysis['Months_Until_Stockout'].apply(lambda x: 1 if x <= months_ahead else 0)
    return df_analysis[['Item_ID', 'Months_Until_Stockout', 'Probability_Stockout_3Months']]

def visualize_months_until_stockout(stockout_estimates):
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Item_ID', y='Months_Until_Stockout', data=stockout_estimates)
    plt.xticks(rotation=90)  # Rotate item IDs for better readability
    plt.title('Estimated Months Until Stockout for Each Item')
    plt.xlabel('Item ID')
    plt.ylabel('Months Until Stockout')
    plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
    plt.show()

def visualize_stockout_probability_distribution(stockout_estimates):
    plt.figure(figsize=(8, 4))
    sns.countplot(x='Probability_Stockout_3Months', data=stockout_estimates)
    plt.title('Distribution of Stockout Probabilities in the Next 3 Months')
    plt.xlabel('Probability of Stockout (1 = High Risk, 0 = Low Risk)')
    plt.ylabel('Number of Items')
    plt.xticks([0, 1], ['Low Risk', 'High Risk'])  # Rename x-axis ticks for clarity
    plt.show()
    
if __name__ == "__main__":
    # Load data from JSON files
    sales_inventory_data = pd.DataFrame(load_data_from_json('./data/sales_inventory_data.json'))
    sales_records_data = pd.DataFrame(load_data_from_json('./data/sales_records_data.json'))

    # Calculate average monthly sales
    avg_monthly_sales = calculate_average_monthly_sales(sales_records_data)

    # Estimate stockout probabilities
    stockout_estimates = estimate_stockout_probability(sales_inventory_data, avg_monthly_sales, 3)

    # Display the results
    print("Estimated Stockout Probabilities in the Next 3 Months:")
    print(stockout_estimates)
    # Visualize the results
    visualize_months_until_stockout(stockout_estimates)
    visualize_stockout_probability_distribution(stockout_estimates)