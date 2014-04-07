#**********************************
# Name: Gedion Y. Metaferia
# Date: 4/7/2014
# file: sentiment.py
#**********************************
"""Includes methods used for sentiment analysis on a list of tweets"""

import csv
import geodata
def sentiment_list(filename):
    """Generates a sentiment dictionary from the given filename
    
    The dictionary maps words to a float between -1 and 1, where 1 is 
    most positive and -1 most negative. The file should be in csv format.
    """
    input_file = open(filename,'rU')
    reader = csv.reader(input_file)
    out = {}
    for line in reader:
    	out[line[0]] = float(line[1])

    return out

def get_sentiment(tweet, sentiments):
    """Calculates sentiment for the given tweet.
    
    tweet is a dictionary representing a single tweet.
    The text of the tweet is splitted into a list of words
    using the tweet_words method from geodata module. The sentiment
    for each tweet is looked up on the dictionary, sentiments.
    If the word is not on the dictionary it is is ignored in calculating
    the average sentiment of the tweet. If all the words on the tweet 
    can't be located on the dictionary the sentiment value will be None.
    """
    words = geodata.tweet_words(tweet)
    found = 0 
    total_sentiment = 0
    for word in words:
        if(word in sentiments):
            total_sentiment += sentiments[word]
            found +=1
    if(found==0):
        return None
    return total_sentiment/found

def add_sentiment(tweets,sentiments):
    """Adds sentiments to each tweet in the list of tweets
        
    tweets is a list of tweets and sentiments is a dictionary of
    words mapped to their sentiment value
    """
    for tweet in tweets:
    	tweet['sentiment'] = get_sentiment(tweet, sentiments)

#Helper method for tweet_filter
def match(tweet, **kwargs):
	"""Checks if the tweet matches the given filter.
    
    The filter options are word, state and zip. Other filters
    are ignored.
	"""
    #check the filter criteria
	has_word = 'word' in kwargs
	has_state = 'state' in kwargs
	has_zip = 'zip' in kwargs

	#temporarily true if at least one filter is defined
	matches = has_word or has_state or has_zip

	#matches is false if at least one criteria is not met
	if(has_word):
		matches = matches and kwargs['word'] in tweet['text']
	if(has_state):
		matches = matches and kwargs['state'].upper() == tweet['state']
	if(has_zip):
		matches = matches and kwargs['zip'] == tweet['zip']

	return matches

def tweet_filter(tweets, **kwargs):
	"""Returns a list of tweets that match the filter criteria.

	The filter options are word, state and zip. state is a two letter indentifier
	of the state and zip is a string of digits. Other filters are
	ignored. 
    """
	filtered =[]
	for tweet in tweets:
		if(match(tweet,**kwargs)):
			filtered.append(tweet)

	return filtered

def avg_sentiment(tweets):
    """Returns the average sentiment of a list of tweets"""
    found = 0 
    total_sentiment = 0
    for tweet in tweets:
        if(tweet['sentiment'] != None):
            total_sentiment += tweet['sentiment']
            found +=1
    if(found==0):
        return None
    return total_sentiment/found

#helper method for most_positive and most_negative
def avg_state(tweets):
    """Return a dictionary of average sentiments by state"""
    count = {}
    total = {}
    avg = {}
    for tweet in tweets:
        state = tweet['state']
 	    #if already in the dictionary just update the values
        if(state in total):
 	        if(tweet['sentiment'] != None):
 	    	    total[state]+=tweet['sentiment']
 	    	    count[state]+=1
 	    #add new state to the dictionary
        else:
        	if(tweet['sentiment'] != None):
        		total[state] = tweet['sentiment']
        		count[state] =1
    #get the average for each
    for state in total:
    	avg[state] = total[state]/count[state]
    
    return avg

def most_positive(tweets, word): 
    """returns the state with the most positive sentiment

    returns a string that is the two-letter postal code for 
    the state with the highest average sentiment for tweets 
    containing word
    """
    filtered = tweet_filter(tweets,word=word)
    state_sentiment = avg_state(filtered)
    maximum = -1
    max_state =""
    for state in state_sentiment:
    	if(state_sentiment[state]>maximum):
    		max_state = state
    		maximum = state_sentiment[state] 

    return max_state

def most_negative(tweets, word): 
    """returns the state with the most negative sentiment

    returns a string that is the two-letter postal code for 
    the state with the lowest average sentiment for tweets 
    containing word
    """
    filtered = tweet_filter(tweets,word=word)
    state_sentiment = avg_state(filtered)
    minimum = 1
    min_state =""
    for state in state_sentiment:
    	if(state_sentiment[state]<minimum):
    		min_state = state 
    		minimum = state_sentiment[state]

    return min_state