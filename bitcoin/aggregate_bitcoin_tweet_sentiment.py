import json
from textblob import TextBlob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

def perform_sentiment_analysis(file_path):
    # Load cleaned tweets
    with open(file_path, 'r', encoding='utf-8') as file:
        tweets = json.load(file)

    # Analyze sentiments and categorize
    sentiments = []
    for tweet in tweets:
        analysis = TextBlob(tweet)
        if analysis.sentiment.polarity > 0:
            sentiments.append("Positive")
        elif analysis.sentiment.polarity < 0:
            sentiments.append("Negative")
        else:
            sentiments.append("Neutral")

    return sentiments

def aggregate_sentiments(sentiments):
    # Aggregate sentiment counts
    sentiment_counts = Counter(sentiments)
    sentiment_counts_df = pd.DataFrame(list(sentiment_counts.items()), columns=['Sentiment', 'Count'])
    return sentiment_counts_df

def plot_sentiment_distribution(sentiment_counts_df):
    # Set the aesthetic style of the plots
    sns.set_style("whitegrid")

    # Create the plot
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Sentiment', y='Count', data=sentiment_counts_df, palette='viridis')

    # Add title and labels
    plt.title('Tweet Sentiment Distribution', fontsize=16)
    plt.xlabel('Sentiment', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.xticks(rotation=45, fontsize=12)  # Rotate the labels for better readability

    # Show the plot
    plt.show()

if __name__ == "__main__":
    file_path = 'cleaned_bitcoin_tweets.json'
    sentiments = perform_sentiment_analysis(file_path)
    sentiment_counts_df = aggregate_sentiments(sentiments)
    plot_sentiment_distribution(sentiment_counts_df)
