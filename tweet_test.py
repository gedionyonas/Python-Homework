#**********************************
# Name: Gedion Y. Metaferia
# Date: 4/7/2014
# file: tweet_test.py
#**********************************
import geodata
import sentiment
import auxillary

def main():
    print "Welcome to tweet analyzer"
    filename = raw_input("Please type in the name of your tweet file: ")
    print "Compiling tweets..."
    tweets = auxillary.tweet_list(filename)

    print "Calculating location data..."
    geodata.add_geo(tweets)

    print "Calculating sentiments..."
    sentiments = sentiment.sentiment_list('sentiments.csv')
    sentiment.add_sentiment(tweets, sentiments)

    outfile = filename[:-4]+"_with_metadata.txt"
    print "Writing to "+outfile+" ..."
    geodata.write_tweets(tweets,outfile)

    print "You can now use the filters"
    
    kwargs = {}
    condition = raw_input("Do you want to filter by words? (y/n): ")
    if(condition.upper() == 'Y'):
    	kwargs['word'] = raw_input("Please insert your word: ")

    condition = raw_input("Do you want to filter by state? (y/n): ")
    if(condition.upper() == 'Y'):
    	kwargs['state'] = raw_input("Please insert the state (use two letters): ")

    condition = raw_input("Do you want to filter by zipcode? (y/n): ")
    if(condition.upper() == 'Y'):
    	kwargs['zip'] = raw_input("Please insert the zipcode: ")

    filtered = sentiment.tweet_filter(tweets,**kwargs)
    outfile = filename[:-4]+"_filtered.txt"

    print "Writing filtered tweets to "+outfile
    geodata.write_tweets(filtered, outfile)
    print "Your filter has an average sentiment of "+str(sentiment.avg_sentiment(filtered))

    if('words' in kwargs):
    	print kwargs['words']+" has been used most positively in "+sentiment.most_positive(tweets,kwargs['words'])\
    	+" and most negatively in "+sentiment.most_negative(tweets,kwargs['words'])
    
    print "Thank You for using the tweet analyzer"

main()