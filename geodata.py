#**********************************
# Name: Gedion Y. Metaferia
# Date: 3/31/2014
# file: geodata.py
#**********************************
import datetime

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
   
    text = " ".join(tweet_list[5:])
    time = make_time(date_string+" "+time_string)
    lat = float(lat_string)
    lon = float(lon_string)

    return {'text':text, 'time':time, 'lat':lat,'lon':lon}
