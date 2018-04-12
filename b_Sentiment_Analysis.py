#!/usr/bin/python35
#encoding:utf-8

# Use Python 3


import json
from pprint import pprint
from textblob import TextBlob 
import matplotlib.pyplot as plt
import pickle
#getting data


def generate_hist(pickle_file, state):
	tweets_list=pickle.load(open(pickle_file,'rb'))
	pollist=[]
	sublist=[]
	for lin in  range(len(tweets_list)) : 
		pollist.append(TextBlob(tweets_list[lin]).polarity)
		sublist.append(TextBlob(tweets_list[lin]).subjectivity)
	#bins=[-1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1]
	#Plotting Polarity score 
	#plt.hist(pollist,bins, histtype='bar',rwidth=0.8,color='b')
	plt.hist(pollist, histtype='bar',rwidth=0.8,color='b')
	
	plt.title('Polarity Score vs Tweet Count Graph for {}\nAverage Polarity:{}'.format(state, (sum(pollist)/len(pollist))))
	plt.xlabel('Polarity Score -------->')
	plt.ylabel('Tweet Count(total tweet={}) -------->'.format(len(pollist)))
	plt.legend()
	plt.savefig('op2_1_polarity_{}_{}.pdf'.format(pickle_file.split('.')[0], state))
	plt.show()
	
	#Plotting Subjectivety score
	#bins=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
	plt.hist(sublist,bins=10, histtype='bar',rwidth=0.8,color='r')
	plt.title('Subjectivity Score vs Tweet Count Graph for {}\nAverage Subjectivity:{}'.format(state, sum(sublist)/len(sublist)))
	plt.xlabel('Subjectivity Score -------->')
	plt.ylabel('Tweet Count (total tweet={}) -------->'.format(len(sublist)))
	plt.legend()
	plt.savefig('op2_2_subjectivity_{}_{}.pdf'.format(pickle_file.split('.')[0], state))
	plt.show()
	
	
	

if __name__=='__main__':
	generate_hist('op1_tweet_stream_location_trump_Texas_cleaned_tweets.pickle', 'Texas')
	
	