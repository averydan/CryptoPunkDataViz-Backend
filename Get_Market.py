import urllib.request
import html2text
import os
import pandas as pd
from sqlalchemy import create_engine

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

#Pandas dataframe cleanup, and exporting to CSV
market_df = pd.read_csv("market_data.txt", sep= ' ', lineterminator='\\', names = ['Date', 'Time', 'id', 'Price ETH'])
punks_df = pd.read_csv("PunkList.csv")

market_df['Date'] = market_df['Date'].str[1:]
market_df['Date'] = market_df['Date'].str.replace(r"[\"\',]",'')
market_df['Price ETH'] = market_df['Price ETH'].str.replace(r"[\"\',]",'')

market_df.to_csv('Market_Data.csv',  index = None)

# Loading into Postgres
engine = create_engine('postgresql://postgres:B9i18O69@localhost:5432/CryptoPunks')
#ENTERPASSWORD
conn = engine.connect()

market_df.to_sql('market_df', engine, index = False)
punks_df.to_sql('punks_df', engine, index = False)
