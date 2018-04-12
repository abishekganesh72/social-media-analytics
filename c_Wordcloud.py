#!/usr/bin/python35
#encoding:utf-8

#use : Python 3

from pprint import pprint
import matplotlib.pyplot as plt
import pickle
from wordcloud import WordCloud
import nltk 
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
from my_stopwords import mystopwords
from pprint import pprint

ps = PorterStemmer()
stopwords = nltk.corpus.stopwords.words('english') + mystopwords
	


def generate_wordcloud(pickle_file,state):
	tweets_list=pickle.load(open(pickle_file,'rb'))
	words_lst=[]
	for tweet in tweets_list:
		words_lst.extend([word for word in [ps.stem(stemed_word) for stemed_word in word_tokenize(tweet)] if word not in stopwords])
		word_stemmed=''
	for word in words_lst:
		word_stemmed+=' '+word
	
		
	
	wordcloud = WordCloud(max_font_size=80).generate(word_stemmed)
	plt.figure()
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.savefig('op3_wordcloud_{}_{}.pdf'.format(pickle_file.split('.')[0], state))
	plt.show()
	
		
# Main
if __name__=='__main__':
	generate_wordcloud('op1_tweet_stream_location_trump_Texas_cleaned_tweets.pickle', 'Texas')
	
	
