# Import the functions from summarizer.py
from summarizer import summarize_text_with_sentiment

# Example text for sentiment analysis
text_for_sentiment = """In the Army, the training period for soldiers before the announcement of the Agnipath scheme was between 37 and 42 weeks.
The reduction of this training period to 24 weeks for Agniveers has been adversely impacting their overall training, according to the feedback received by the Army.
The Army is discussing that the training duration for Agniveers be increased to what it was originally for soldiers, while increasing the overall service period to around seven years from the current four years, so that gratuity and ex-servicemen (ESM) status could be granted to them.
The move, if implemented, will also make Agniveers eligible for benefits applicable to ESM and the entire period of seven years of service as Agniveers will then likely be counted as part of pensionable service for those getting permanently retained in the force."
"""



# Perform text summarization
summary,label,score = summarize_text_with_sentiment(text_for_sentiment)
print(summary)
print('sentiment:-',label)
print('score:-',score)
