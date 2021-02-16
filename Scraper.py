from bs4 import BeautifulSoup
import pandas as pd
import requests
import time


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

    maxvalue = df['Amount (USD)'].idxmax()

    print(df.loc[[maxvalue]])
    time.sleep(60)

