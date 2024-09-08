from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load('models/sentiment_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        review_vectorized = vectorizer.transform([review])
        prediction = model.predict(review_vectorized)[0]
        return render_template('result.html', review=review, sentiment=prediction)

if __name__ == '__main__':
    app.run(debug=True)