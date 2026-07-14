import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


with open("intents.json", "r") as file:
    data = json.load(file)


commands = []
labels = []


for intent, examples in data.items():
    for example in examples:
        commands.append(example)
        labels.append(intent)


vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(commands)


model = MultinomialNB()

model.fit(X, labels)


def predict_intent(text):

    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)[0]

    confidence = model.predict_proba(text_vector).max()

    return prediction, confidence