#**********************************
# Name: Gedion Y. Metaferia
# Date: 4/2/2014
# file: auxillary.py
#**********************************

"""Includes auxillary methods for geodata module"""

import csv
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

def tweets_from_list(strlist):
    """Compile a list of tweet dictionaries from a list of strings"""
    tweet_list = []
    #avoid cross import conflicts
    from geodata import make_tweet
    for tweet in strlist:
        tweet_list.append(make_tweet(tweet))

    return tweet_list

def zips_from_list(strlist):
    """Compile a list of zip info dictionaries from a list of strings"""
    zip_list = []
    from geodata import make_zip
    for location in strlist[1:]:
        zip_list.append(make_zip(location))

    return zip_list

def tweet_list(filename):
    """Compile a list of tweets from the tweet file with name <filename>
       
       The tweets are represented as dictionaries
    """
    input_file = open(filename,'rU')
    reader = csv.reader(input_file,dialect = csv.excel_tab)
    tweets =[]

    #buffer to handle unexcpected new lines
    buf= "\t".join(reader.next())
    while buf!="":
        line = buf
        buf = ""
        try:
            #next throws Stop Iteration if no element to go through
            buf = "\t".join(reader.next())  
            while(buf[0]!='['):
                line+=buf
                buf = "\t".join(reader.next())
        except StopIteration:
            pass   
        finally:
            tweets.append(line)
    input_file.close()
    return tweets_from_list(tweets)

def zip_list(filename):
    """Compile a list of zip code information from the csv file with name <filename>

       The returned values are dictionaries
    """

    input_file = open(filename,'rU')
    reader = csv.reader(input_file)
    zips =[]
    for line in reader:
        zips.append(line)
    input_file.close()
    return zips_from_list(zips)
    
