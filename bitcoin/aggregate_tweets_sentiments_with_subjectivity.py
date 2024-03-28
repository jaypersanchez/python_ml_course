import json
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load tweets from the JSON file
with open('data/cleaned_bitcoin_tweets.json', 'r') as file:
    tweets = json.load(file)

# Initialize counters
positive_count = 0
neutral_count = 0
negative_count = 0
subjective_count = 0
objective_count = 0

# Function to analyze sentiment
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity
    if subjectivity >= 0.5:
        # Counting subjective tweets
        global subjective_count
        subjective_count += 1
    else:
        # Counting objective tweets
        global objective_count
        objective_count += 1

    if polarity > 0:
        return 'Positive'
    elif polarity == 0:
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
print(f"Subjective: {subjective_count}, Objective: {objective_count}")

# Data to plot for sentiment
labels = 'Positive', 'Neutral', 'Negative'
sizes = [positive_count, neutral_count, negative_count]
colors = ['lightgreen', 'gold', 'lightcoral']
explode = (0.1, 0, 0)  # explode 1st slice

# Plot for sentiment
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Sentiment Analysis of Bitcoin Tweets Subjective vs. Objective')
plt.show(block=False)

# **** Data to plot for subjectivity ***
labels = 'Subjective', 'Objective'
sizes = [subjective_count, objective_count]
colors = ['skyblue', 'orange']
explode = (0.1, 0)  # explode 1st slice

# Plot for subjectivity
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Subjectivity Analysis of Bitcoin Tweets')
plt.show()
