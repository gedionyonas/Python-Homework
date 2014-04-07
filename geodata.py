#**********************************
# Name: Gedion Y. Metaferia
# Date: 4/2/2014
# file: geodata.py
#**********************************
import string
from math import sin, cos, sqrt, asin, radians
import csv
from auxillary import make_time, zip_list

#average radius of the earth in miles
Re =3959
MAX_DISTANCE = 250


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
    state   -- A string; Two-letter postal code for state
    lat    -- A number; latitude of zip code location
    lon    -- A number; longitude of zip code location
    city   -- A string; name of city assoicated with zip code
  

    """
    #remove quote character and spaces
    for i in range(len(zipcode)):
    	zipcode[i] = zipcode[i].strip()
    	zipcode[i] = zipcode[i].strip('\"')
    	zipcode[i] = zipcode[i].strip()

    lat = float(zipcode[2].strip())
    lon = float(zipcode[3].strip())

    return {'zip':zipcode[0], 'state':zipcode[1],'lat':lat,'lon':lon,'city':zipcode[4]}

def find_zip(tweet, zip_list):
    """return zipcode associated with a tweets location data
    zip_list is a list of zip_cides represented as dictionaries"""
    
    tweet_loc = tweet_location(tweet)
    closest = geo_distance(tweet_loc, (zip_list[0]['lat'], zip_list[0]['lon']))
    closest_zip = zip_list[0]

    for i in range(1, len(zip_list)): 
        zip_loc = (zip_list[i]['lat'], zip_list[i]['lon']) 
        dist = geo_distance (tweet_loc,zip_loc) # calculate distance
        if dist < closest: # repeat loop if this is not the closest zipcode
            closest = dist
            closest_zip = zip_list[i]

    # for zipcodes outside the US
    if(closest > MAX_DISTANCE):
    	closest_zip = {'zip':'00000','state':'INTL','lat':tweet['lat'],'lon':tweet['lon'],'city':"international"}

    return closest_zip

def geo_distance(loc1,loc2):
    """Return the great circle distance (in miles) between two
    tuples of (latitude,longitude)

    Uses the "haversine" formula.
    http://en.wikipedia.org/wiki/Haversine_formula"""
    lat1 = loc1[0]
    lat2 = loc2[0]
    lon1 = loc1[1]
    lon2 = loc2[1]
    
    dlat,dlon = radians(lat2-lat1),radians(lon2-lon1)
    lat1, lat2= radians(lat1),radians(lat2) # change to radians

    h = sin((dlat)/2)**2 + cos(lat1)*cos(lat2)*sin((dlon)/2)**2
    d =2*Re*asin(sqrt(h))

    return d
def add_geo(tweets):
    """adds the new keys state and zip to each tweet dictionary in the list tweets"""
    zips = zip_list('zips.csv')
    for tweet in tweets: # loop through the tweets list and replace.
        zipcode = find_zip(tweet, zips)
        tweet['zip'] = zipcode['zip']
        tweet['state']= zipcode['state']
   
def write_tweets(tweets,outfile):
    """writes the list of tweets to a text file with name outfile"""
    out = open(outfile,'w')
    for tweet in tweets:
        loc = tweet_location(tweet)
        out.write('['+str(loc[0])+', '+str(loc[1])+']\t')
        out.write('6\t')
        out.write(tweet_time(tweet).strftime('%Y-%m-%d %H:%M:%S')+'\t')

        if('zip' in tweet):
            out.write(tweet['state']+" "+tweet['zip']+"\t")
        out.write(tweet_text(tweet)+"\n")

    out.close()