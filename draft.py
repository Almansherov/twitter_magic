from textblob import TextBlob
wiki = TextBlob("Alman is never late to work")
print(wiki.tags)
print(wiki.words)

print(wiki.sentiment.polarity)