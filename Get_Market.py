import urllib.request
import html2text
import os
import pandas as pd

webUrl  = urllib.request.urlopen('http://subopt.org/priceseth.txt')

#get the result code and print it
#print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
data = webUrl.read()
#print (data)

newfile = 'market_data.txt'
open(newfile, 'w').close()


create = open(newfile, "w")
create.write(str(data))
create.close()

#Pandas dataframe for CSV
market_df = pd.read_csv("market_data.txt", sep= ' ', lineterminator='\\', names = ['Date', 'Time', 'ID', 'Price ETH'])

market_df['Date'] = market_df['Date'].str[1:]
market_df['Date'] = market_df['Date'].str.replace(r"[\"\',]",'')
market_df['Price ETH'] = market_df['Price ETH'].str.replace(r"[\"\',]",'')

market_df.to_csv('Market_Data.csv',  index = None)