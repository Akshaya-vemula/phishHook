import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("phishing_dataset.csv")

X = data["email"]
y = data["label"]

# Convert text to numbers
vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vectorized, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained successfully!")