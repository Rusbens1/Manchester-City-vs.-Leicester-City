import pandas as pd
import seaborn as sns
import numpy as np
import json

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer




def sentiment_score_analyzer(df):
    if df['lang'] == 'en' and df['cleaned_tweet']:
        tweet = str(df['cleaned_tweet'])
        blob = TextBlob(tweet, analyzer= NaiveBayesAnalyzer())
        sent_score = blob.sentiment[1]
        score = round(sent_score, 2)
        print tweet
        print score
        return round(sent_score, 2)
    else:
    	print 'N/A'
        return 'N/A'


sentiment_df = pd.read_csv('sentiment.csv')

sentiment_df['sent_score'] = sentiment_df.apply(sentiment_score_analyzer, axis = 1)

sentiment_df.to_csv('sentiment_scores.csv', encoding = 'utf-8')


		
	


