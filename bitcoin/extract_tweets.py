import json

# Load the dataset
with open('sentiment_dataset.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract tweets from the "input" field
tweets = [item['input'] for item in data]

# Save the extracted tweets to a new JSON file
with open('bitcoin_tweets.json', 'w', encoding='utf-8') as file:
    json.dump(tweets, file, indent=4)

print("Extracted tweets have been saved to bitcoin_tweets.json")
