import csv

def tweet_list(filename):
    input_file = open(filename,'rU')
    reader = csv.reader(input_file,dialect = csv.excel_tab)
    tweets =[]
    for list in reader:
        line = "\t".join(list)
        tweets.append(line)
    input_file.close()
    return tweets

def zip_list(filename):
    input_file = open(filename,'rU')
    reader = csv.reader(input_file)
    zips =[]
    for line in reader:
        tweets.append(line)
    input_file.close()
    return zips