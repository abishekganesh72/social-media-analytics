

#python3 
from a_Clean_Tweets import clean_tweets
from b_Sentiment_Analysis import generate_hist
from c_Wordcloud import generate_wordcloud
from d1_TopicModeling import generate_topics_NMF

#save_loc = clean_tweets('data/tweet_stream_logan_1000_2.json')
save_loc = clean_tweets('tweet_stream_location_trump_Misc.json')
#save_loc = clean_tweets('data/tweet_stream_trump_10000_2.json')
generate_hist(save_loc, 'GA_FL')
generate_wordcloud(save_loc, 'GA_FL')
generate_topics_NMF(save_loc, 'GA_FL',10)