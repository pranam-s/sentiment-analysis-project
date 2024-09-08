from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the model and vectorizer
try:
    model = joblib.load('models/sentiment_model.pkl')
    vectorizer = joblib.load('models/vectorizer.pkl')
except FileNotFoundError:
    print("Error: Model files not found. Please run model_trainer.py first.")
    exit(1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        if not review:
            return render_template('index.html', error="Please enter a review.")
        try:
            review_vectorized = vectorizer.transform([review])
            prediction = model.predict(review_vectorized)[0]
            return render_template('result.html', review=review, sentiment=prediction)
        except Exception as e:
            return render_template('index.html', error=f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)