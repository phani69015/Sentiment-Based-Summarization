# summarizer.py
from transformers import pipeline
 
SENTIMENT_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"
SUMMARIZATION_MODEL = "facebook/bart-large-cnn"
 
sentiment_analyzer = pipeline("sentiment-analysis", model=SENTIMENT_MODEL)
summarizer = pipeline("summarization", model=SUMMARIZATION_MODEL)
def analyze_sentiment(text):
    sentiment = sentiment_analyzer(text)
    return sentiment[0]['label'], sentiment[0]['score']

def add_sentiment_phrases(text, sentiment_label):
    if sentiment_label == 'POSITIVE':
        # Add positive sentiment phrases
        text += " Excellent ! This is a great News."
    elif sentiment_label == 'NEGATIVE':
        # Add negative sentiment phrases
        text += " Unfortunately, this isn't a good news."
    else:
        # Add neutral sentiment phrases
        text += " Overall, this seems to be an general day news."
    
    return text

def summarize_text_with_sentiment(text):
    # Perform sentiment analysis
    sentiment_label, sentiment_score = analyze_sentiment(text)
    
    # Adjust max_length based on sentiment
    max_length = 150 if sentiment_label == 'POSITIVE' else 100
    
    # Generate summary
    summary = summarizer(text, max_length=max_length, min_length=30, do_sample=False)
    
    # Include sentiment-specific phrases in the summary
    summary_text = add_sentiment_phrases(summary[0]['summary_text'], sentiment_label)
    
    return summary_text,sentiment_label, sentiment_score
