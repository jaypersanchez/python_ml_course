import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def preprocess_data(file_path):
    try:
        df = pd.read_json(file_path)
        print("Dataset loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def plot_sentiment_distribution(df):
    # Ensure the DataFrame is not empty
    if df is not None:
        # Count the occurrences of each sentiment
        plt.figure(figsize=(8, 6))
        sns.countplot(x='output', data=df, palette='viridis')
        plt.title('Sentiment Distribution in Tweets')
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        plt.xticks(rotation=45)  # Adjust rotation if necessary
        plt.show()
    else:
        print("DataFrame is empty. Cannot plot sentiment distribution.")

if __name__ == "__main__":
    print("Current Working Directory:", os.getcwd())
    file_path = 'sentiment_dataset.json'
    df = preprocess_data(file_path)
    plot_sentiment_distribution(df)
