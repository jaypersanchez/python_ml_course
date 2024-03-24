import json
from textblob import TextBlob

# Load tweets from the JSON file
with open('data/cleaned_bitcoin_tweets.json', 'r') as file:
    tweets = json.load(file)

# Initialize counters
positive_count = 0
neutral_count = 0
negative_count = 0

# Function to analyze sentiment
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Analyze sentiment of each tweet and update counters
for tweet in tweets:
    sentiment = analyze_sentiment(tweet)
    if sentiment == 'Positive':
        positive_count += 1
    elif sentiment == 'Neutral':
        neutral_count += 1
    else:  # Negative
        negative_count += 1

# Print the counts to the console
print(f"Positive: {positive_count}, Neutral: {neutral_count}, Negative: {negative_count}")
