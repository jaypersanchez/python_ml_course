import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'cleaned_sentiment_dataset.json'
df = pd.read_json(file_path)

# Count the occurrences of each sentiment
sentiment_counts = df['output'].value_counts()

# Plot the sentiment distribution
plt.figure(figsize=(8, 6))
sentiment_counts.plot(kind='bar', color=['green', 'blue', 'red'])
plt.title('Sentiment Distribution in Tweets')
plt.xlabel('Sentiment')
plt.ylabel('Frequency')
plt.xticks(rotation=0)  # Rotate labels to be horizontal
plt.show()
