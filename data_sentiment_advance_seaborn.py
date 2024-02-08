import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'sentiment_dataset.json'
df = pd.read_json(file_path)

# Set the overall aesthetics
sns.set_theme(style="whitegrid")  # Set a theme for nicer plots

# Create a more detailed count plot
plt.figure(figsize=(8, 6))
ax = sns.countplot(x='output', data=df, palette='coolwarm', order = df['output'].value_counts().index)

# Customizing with Seaborn and adding annotations
ax.set_title('Sentiment Distribution in Tweets', fontsize=16)  # Use Seaborn's set_title for the title
ax.set_xlabel('Sentiment', fontsize=14)
ax.set_ylabel('Count', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)

# Adding annotations on each bar
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')

plt.tight_layout()  # Adjust layout to not cut off elements
plt.show()
