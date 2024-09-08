# Movie Review Sentiment Analysis

This project demonstrates a simple sentiment analysis model for movie reviews using Python, scikit-learn, and Flask.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/sentiment-analysis-project.git
   cd sentiment-analysis-project
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Generate the sample data:
   ```
   python data_generator.py
   ```

5. Train the model:
   ```
   python model_trainer.py
   ```

6. Run the Flask app:
   ```
   python app.py
   ```

7. Open your web browser and go to `http://localhost:5000` to use the sentiment analysis tool.

## Project Structure

- `data_generator.py`: Generates sample movie reviews and sentiments.
- `model_trainer.py`: Trains the sentiment analysis model using the generated data.
- `app.py`: Flask application for serving the web interface.
- `templates/`: Contains HTML templates for the web interface.
- `static/`: Contains CSS files for styling the web interface.
- `data/`: Stores the generated movie reviews CSV file.
- `models/`: Stores the trained model and vectorizer.

## Usage

1. Enter a movie review in the text area on the home page.
2. Click "Analyze Sentiment" to get the predicted sentiment.
3. View the result and analyze another review if desired.
