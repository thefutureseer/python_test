# Description: Analyze the sentiment of a given text.
# Input: A string of text (e.g., "I love Python!").
# Output: Positive, Neutral, or Negative sentiment.
from textblob import TextBlob

text = "I love Python programming!"
analysis = TextBlob(text)
sentiment = "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"
print(f"Sentiment: {sentiment}")
