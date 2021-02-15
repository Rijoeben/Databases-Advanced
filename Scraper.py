from bs4 import BeautifulSoup
import pandas as pd
import requests

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
            hashes.append(i.text[4:])
        if("Time" in i.text):
            times.append(i.text[4:])
        if("Amount (BTC)" in i.text):
            btc.append(i.text[12:])
        if("Amount (USD)" in i.text):
            s = i.text[13:-3]
            f = float(s)
            usd.append(s)

d = {'Hash': hashes, 'Time': times, 'Amount (BTC)': btc, 'Amount (USD)':usd}
df = pd.DataFrame(data=d)

print(df)

#maxvalue = df['Amount (USD)'].idxmax()

#print(df[maxvalue])