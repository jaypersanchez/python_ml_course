import pandas as pd
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
    if df is not None:
        # Count the occurrences of each sentiment
        sentiment_counts = df['output'].value_counts()

        # Plot the sentiment distribution
        plt.figure(figsize=(8, 6))
        sentiment_counts.plot(kind='bar', color=['skyblue', 'limegreen', 'salmon'])
        plt.title('Tweetier Sentiments with MatPlotLib')
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        plt.xticks(rotation=0)  # Keep labels horizontal for clarity
        plt.show()
    else:
        print("DataFrame is empty. Cannot plot sentiment distribution.")

if __name__ == "__main__":
    print("Current Working Directory:", os.getcwd())
    file_path = 'sentiment_dataset.json'
    df = preprocess_data(file_path)
    plot_sentiment_distribution(df)
