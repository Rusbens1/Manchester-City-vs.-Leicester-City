#**Leicester City FC vs. Manchester City FC**
##*Twitter Exploratory and Sentiment Analysis*

###Match Info:
- Kickoff: Tuesday, December 29, 2015 - 2:45 PM ET
- League: Barclays Premier League
- Venue: King Power Stadium
- Location: Leicester, England
- Final Score: 
    - Leicester City FC - 0
    - Manchester City FC - 0

###Introduction

To analyze the Twitter-sphere's reaction to the match. I did so by first performing some exploratory analysis on the collection of tweets, as well as some sentiment analysis on  from both during and after the match per respective team, and period during the match.


### Methodology

1. Collected around 16,000 tweets using Python 2.7 and the Twitter streaming API ranging from the end of halftime until 10 minutes after full time.
2. Performed exploratory data analysis and seaborn plots to understand the profile of my collection of tweets.
3. Ran a sentiment analysis on each eligible tweet using the Naive Bayes Analyzer from the TextBlob library.
4. Analyzed the results of my sentiment analysis per team and time period of the match to determine the average sentiment.