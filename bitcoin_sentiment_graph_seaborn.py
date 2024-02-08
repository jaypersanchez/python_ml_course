import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'cleaned_sentiment_dataset.json'
df = pd.read_json(file_path)

# Plot the sentiment distribution using Seaborn
plt.figure(figsize=(8, 6))
sns.countplot(x='output', data=df, palette='viridis')
plt.title('Sentiment Distribution in Tweets')
plt.xlabel('Sentiment')
plt.ylabel('Frequency')
plt.xticks(rotation=45)  # Adjust rotation if necessary

plt.show()
