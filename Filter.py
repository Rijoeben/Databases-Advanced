from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import pymongo as mongo
import redis
import json

#Mijn filter gaat ervanuit dat hij wordt gestart wanneer het scrapen stopt. Zodat ik dus alle data uit 1 scrape sessie kan behandelen en doorsturen naar de mongodb
client = mongo.MongoClient("mongodb://127.0.0.1:27017")
bitcoin_db = client["bitcoins"]
col_high = bitcoin_db["Highest"]

r = redis.Redis(host='localhost',port=6379, db=0)

l = r.llen("Scrapes")

data = r.lrange("Scrapes",0,l)

frameList = []

for x in data:
    df = pd.read_json(x)
    frameList.append(df)

df = pd.concat(frameList, ignore_index = True)

print(df)

uniqueTimes = df['Time'].unique()

for time in uniqueTimes:
    df1 = df.where(df['Time'] == time)
    maxvalue = df1['Amount (USD)'].idxmax()
    df2 = df1.loc[[maxvalue]]


    max_hash = df2["Hash"].item()
    max_time = df2["Time"].item()
    max_btc = df2["Amount (BTC)"].item()
    max_usd = df2["Amount (USD)"].item()

    data = { "Hash": max_hash, "Time": max_time, "Amount (BTC)": max_btc, "Amount (USD)": max_usd}
    col_high.insert_one(data)