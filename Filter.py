from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import pymongo as mongo
import redis
import json


r = redis.Redis(host='localhost',port=6379, db=0)

l = r.llen("Scrapes")

data = r.lrange("Scrapes",0,l)

frameList = []

for x in data:
    df = pd.read_json(x)
    frameList.append(df)

df = pd.concat(frameList, ignore_index = True)

print(df)