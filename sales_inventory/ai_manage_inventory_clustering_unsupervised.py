"""
Clustering analysis is a type of unsupervised learning, not supervised learning. 
Unlike supervised learning, where we have input data along with corresponding output labels 
and we train the model to learn the relationship between them, 
unsupervised learning deals with data without labeled responses. 
Clustering aims to group a set of objects in such a way that objects in the 
same group (called a cluster) are more similar to each other than to those in other groups.
"""
"""
Now, we decided to sort these toys into three smaller boxes based on their price tags and 
stickers, so toys that are kind of alike end up together:

Box 0 (Big Price Tag Box): We put all the toys with big price tags here. 
These toys are quite expensive, like your big remote-controlled car, 
and they have a little sticker for a small discount. There are 30 toys in this box.

Box 1 (Small Price Tag Box): This box is for toys with small price tags, 
like your tiny cars or small snack packets. 
They also have a little sticker for a small discount. We found 34 toys like this.

Box 2 (Medium Price Tag Box): The toys with price tags that are not too big and not too 
small go here, like your medium-sized teddy bear. 
These toys also have a little discount sticker. There are 36 toys in this box.

Each box has toys that are similar in how much they cost and how big their discount sticker is. We sorted them into boxes so it's easier to find what you're looking for when you play shop!

Big Price Tag Box (Box 0) has the most expensive toys with a bit of a discount.
Small Price Tag Box (Box 1) has the cheapest toys, also with a bit of a discount.
Medium Price Tag Box (Box 2) has toys that are in the middle, price-wise, and also come with a small discount.

And that's how we sorted your toys into three boxes based on their price tags and discount stickers!
"""
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Assuming avg_sales_by_discount contains the average sales volume for each discount rate
# For clustering, let's use the entire sales_inventory_data for features like Price and Discount_Rate

def load_data_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
    
# Load sales_inventory_data
sales_inventory_data = pd.DataFrame(load_data_from_json('./data/sales_inventory_data.json'))

# Select features for clustering
features_for_clustering = sales_inventory_data[['Price', 'Discount_Rate']]

# Perform KMeans Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
sales_inventory_data['Cluster'] = kmeans.fit_predict(features_for_clustering)

# Print results to console
# Output the first few rows of sales_inventory_data to console including the cluster assignments
print(sales_inventory_data.head())

# If you want to see how many items are in each cluster, you can use value_counts()
print("\nItems in each cluster:")
print(sales_inventory_data['Cluster'].value_counts())

# To get a better understanding of the cluster characteristics, you might want to look at the average
# price and discount rate for items in each cluster:
cluster_centers = pd.DataFrame(kmeans.cluster_centers_, columns=['Price', 'Discount_Rate'])
print("\nCluster Centers (Average Price and Discount Rate):")
print(cluster_centers)

# Visualize the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=sales_inventory_data, x='Price', y='Discount_Rate', hue='Cluster', palette='viridis', legend='full')
plt.title('Clustering of Items Based on Price and Discount Rate')
plt.xlabel('Price')
plt.ylabel('Discount Rate')
plt.show()
