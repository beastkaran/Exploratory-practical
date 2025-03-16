# Import necessary libraries
pip3 install pandas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from flask import Flask, render_template, request
import spacy

# Load your dataset
df = pd.read_csv('your_dataset.csv')

# Data Preprocessing
df = df.dropna()
df['text'] = df['text'].apply(lambda x: clean_text(x))  # Replace clean_text with your text cleaning function

# NLP - Extract features
nlp = spacy.load("en_core_web_sm")

def extract_features(text):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    sentiment = doc.sentiment.polarity
    return tokens, sentiment

# Machine Learning - Train a basic classification model
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['traits'], test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

predictions = model.predict(X_test_vectorized)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy}")

# Flask App - User Interface
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form.get('user_input')
    # Process user input and use the trained model to make predictions
    # Display the predicted personality traits to the user
    return render_template('result.html', predictions=predictions)

if __name__ == '__main__':
    app.run(debug=True)
