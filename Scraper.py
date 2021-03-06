from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import pymongo as mongo
import redis

r = redis.Redis(host='container2',port=6379, db=0)
#r = redis.Redis(host='localhost',port=6379, db=0)

#r.delete("Scrapes")

def scrape():

    while True:
        url = "https://www.blockchain.com/btc/unconfirmed-transactions"

        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find('div',class_="sc-20ch6p-0 beTSoK")

        hashes = []
        times = []
        btc =  []
        usd = []

        for element in results:
            for i in element:
                if("Hash" in i.text):
                    if i.text[4:] != '':
                        hashes.append(i.text[4:])
                if("Time" in i.text):
                    if i.text[4:] != '':
                        times.append(i.text[4:])
                if("Amount (BTC)" in i.text):
                    if i.text[12:] != '':
                        btc.append(i.text[12:])
                if("Amount (USD)" in i.text):
                    s = i.text[13:-3]
                    if s != '':
                        l = s.replace(",","")
                        f = float(l)
                        usd.append(f)
                    

        d = {'Hash': hashes, 'Time': times, 'Amount (BTC)': btc, 'Amount (USD)':usd}
        df = pd.DataFrame(data=d)
        #json = df.to_json()
        

        json_records = df.to_json(orient ='records') 
        
        r.rpush('Scrapes', json_records)
        print("done")

        #r.setex('data',60, json_records)
        #print("json_records = ", json_records, "\n") 

        #maxvalue = df['Amount (USD)'].idxmax()
        #df1 = df.loc[[maxvalue]]


        #max_hash = df1["Hash"].item()
        #max_time = df1["Time"].item()
        #max_btc = df1["Amount (BTC)"].item()
        #max_usd = df1["Amount (USD)"].item()

        #data = { "Hash": max_hash, "Time": max_time, "Amount (BTC)": max_btc, "Amount (USD)": max_usd}
        #col_high.insert_one(data)
        time.sleep(60)

scrape()

