from gensim import corpora, models, similarities, matutils
import re
import nltk
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import  CountVectorizer
import json
import pickle
# for logging
import logging
import string


#logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
#logging.root.level = logging.INFO

#tweet_stream_trump_cleaned_tweets.pickle


tweets =json.load(open('tweet_stream_location_trump_Texas.json','r'))
print(type(tweets))
from nltk.corpus import inaugural
docs = []

from nltk.stem.lancaster import LancasterStemmer
ls = LancasterStemmer()

from nltk.corpus import stopwords
stopwords = nltk.corpus.stopwords.words('english')+[u'rt',u'donald',u'trump',u'tweet', u'retweet', u'realdonaldtrump', 'tweet']

print('getting data')
print('Cleaning data')

for tweet in tweets[:100]:
    #print(tweet, type(tweet))
    cln_tweet = ''
    tweet=re.sub(r'http.://[\w].co/[\w]+',r' ',tweet)
    for punc in string.punctuation:
        tweet = tweet.replace(punc,' ')
    for dig in string.digits:
        tweet = tweet.replace(dig,' ')
    for word in nltk.word_tokenize(tweet.lower()):
        if word not in stopwords:
            #cln_tweet+=' {}'.format(ls.stem(word))
            cln_tweet+=' {}'.format(word)    
    #print(cln_tweet)
    docs.append(cln_tweet.split())

print(len(docs))
#print(docs)


print('Gensim data')

from gensim import corpora
dic  = corpora.Dictionary(docs)
print(dic)


corpus = [dic.doc2bow(text) for text in docs]
#print(corpus[:20])
from gensim import models

tfidf = models.TfidfModel(corpus)
#print(type(tfidf))

corpus_tfidf = tfidf[corpus]

NUM_TOPICS = 10
print(NUM_TOPICS)
print('Working on LDA Model')

model = models.ldamodel.LdaModel(corpus_tfidf, num_topics=NUM_TOPICS, id2word=dic, update_every=1, passes=1500)


print('LDA Model')

topics_found = model.print_topics(10)
counter = 1
for t in topics_found:
    print('Topic #{} {}'.format(counter, t))
    counter+=1
    

print('Working on LSI Model')

print('LSI Model')
model = models.lsimodel.LsiModel(corpus_tfidf, id2word=dic, num_topics=NUM_TOPICS)

model.print_topics()




#model  = gensim.models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negtive300.bin', binary=True)


'''
model  = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

ret = model.most_similar(positive=['woman', 'king'], negative=['man'])
print(ret, type(ret))
for word, conf in ret: printn(word, conf)


'''
