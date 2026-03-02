import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
df = pd.read_csv("spam.csv", encoding="latin-1")

# Keep only first two columns
df = df.iloc[:, :2]

# Rename columns safely
df.columns = ["label", "text"]

# Clean labels
df["label"] = df["label"].astype(str).str.strip().str.lower()

# Features and labels
X = df["text"]
y = df["label"].map({"ham": 0, "spam": 1})   # ADDED

# Vectorizer
cv = CountVectorizer()
X_vect = cv.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vect, y)

# Save model
pickle.dump(model, open("spam.pkl", "wb"))
pickle.dump(cv, open("vectorizer.pkl", "wb"))

print("Model retrained and saved successfully")
