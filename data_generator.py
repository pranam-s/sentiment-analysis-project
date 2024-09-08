import pandas as pd
import numpy as np

def generate_reviews():
    np.random.seed(42)
    
    positive_words = [
    'amazing', 'excellent', 'fantastic', 'great', 'wonderful', 'brilliant', 'outstanding',
    'superb', 'incredible', 'marvelous', 'exceptional', 'phenomenal', 'terrific', 'fabulous',
    'splendid', 'magnificent', 'remarkable', 'extraordinary', 'spectacular', 'sublime'
    ]
    negative_words = [
    'terrible', 'awful', 'disappointing', 'bad', 'horrible', 'poor', 'dreadful',
    'abysmal', 'atrocious', 'disastrous', 'appalling', 'dreadful', 'lousy', 'unacceptable',
    'inferior', 'subpar', 'unsatisfactory', 'inadequate', 'deplorable', 'ghastly'
    ]
    neutral_words = [
    'okay', 'average', 'mediocre', 'fair', 'decent', 'moderate', 'passable', 'fine',
    'ordinary', 'standard', 'typical', 'common', 'unremarkable', 'middling', 'so-so',
    'tolerable', 'acceptable', 'satisfactory', 'sufficient', 'adequate'
    ]

    reviews = []
    sentiments = []

    for _ in range(100):
        sentiment = np.random.choice(['positive', 'negative', 'neutral'])
        if sentiment == 'positive':
            words = np.random.choice(positive_words, size=np.random.randint(3, 6), replace=True)
        elif sentiment == 'negative':
            words = np.random.choice(negative_words, size=np.random.randint(3, 6), replace=True)
        else:
            words = np.random.choice(neutral_words, size=np.random.randint(3, 6), replace=True)
        
        review = f"This movie was {' and '.join(words)}."
        reviews.append(review)
        sentiments.append(sentiment)

    df = pd.DataFrame({'review': reviews, 'sentiment': sentiments})
    df.to_csv('data/movie_reviews.csv', index=False)
    print("Generated 100 movie reviews and saved to data/movie_reviews.csv")

if __name__ == "__main__":
    generate_reviews()