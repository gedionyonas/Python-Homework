#**********************************
# Name: Gedion Y. Metaferia
# Date: 3/31/2014
# file: geodata.py
#**********************************
import datetime
import string

#helper methods for make_tweet
def make_time(date_string):
    """Return a datetime object of the date represented in the string"""
    
    date_time_list = date_string.split()
    date_list = date_time_list[0].split('-')
    time_list = date_time_list[1].split(':')
    
    year=int(date_list[0])
    month=int(date_list[1])
    day=int(date_list[2])
    
    hour=int(time_list[0])
    minute=int(time_list[1])
    second=int(time_list[2])
    
    return datetime.datetime(year,month,day,hour,minute,second)

def make_tweet(tweet_line):
    """Return a tweet, represented as a python dictionary.
    tweet_line: a string corresponding to a line formatted as in all_tweets.txt

    Dictionary keys:
    text  -- A string; the text of the tweet, all in lowercase
    time  -- A datetime object; the time that the tweet was posted
    lat   -- A number; the latitude of the tweet's location
    lon   -- A number; the longitude of the tweet's location

    """
    tweet_list = tweet_line.split()
    lat_string = tweet_list[0][1:-1]
    lon_string = tweet_list[1][:-1]
    date_string = tweet_list[3]
    time_string = tweet_list[4]
   
    text = " ".join(tweet_list[5:]).lower()
    time = make_time(date_string+" "+time_string)
    lat = float(lat_string)
    lon = float(lon_string)

    return {'text':text, 'time':time, 'lat':lat,'lon':lon}

def tweet_text(tweet):
    """Return the text of a tweet as a string"""
    return tweet['text']

def tweet_words(tweet):
    """Return a list of the words in the text of a tweet not
    including punctuation."""
    
    #removes all punctuation marks from tweet['text']
    tweet_string = tweet['text'].translate(None,string.punctuation) 
    return tweet_string.split()


def tweet_time(tweet):
    """Return the datetime that represents when the tweet was posted."""
    return tweet['time']

def tweet_location(tweet):
    """Return an tuple that represents the tweet's location."""
    return (tweet['lat'], tweet['lon'])

def make_zip(zipcode):
    """Return a zip code, represented as a python dictionary.
    zipcode: a list containing a single zip codes data ordered as in zips.csv

    Dictionary keys:
    zip    -- A string; the zip code
    atate   -- A string; Two-letter postal code for state
    lat    -- A number; latitude of zip code location
    lon    -- A number; longitude of zip code location
    city   -- A string; name of city assoicated with zip code
  

    """
    lat = float(zipcode[2])
    lon = float(zipcode[3])

    return {'zip':zipcode[0], 'atate':zipcode[1],'lat':lat,'lon':lon,'city':zipcode[4]}

