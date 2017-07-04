import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('https://en.wikipedia.org/wiki/List_of_towns_in_England')

soup = BeautifulSoup(r.content,'html.parser')

title = soup.title
title_stripped = soup.robots
links = soup.find_all('a')
h1 = soup.find('h1').text
h2 = soup.find_all('h2')


table = soup.find("table")

records = []
# Finds each row and puts it into a record
for tr in table.find_all("tr")[1:]:
    trs = tr.find_all("td")
    record = []
    record.append(trs[0].text)
    record.append(trs[1].text)
    record.append(trs[2].text)
    record.append(trs[0].a["href"])
    records.append(record)

# Finds the headings and puts them into a list to pass to columns of dataframe & makes them match
header = table.find("tr").text
headings = header.split('\n')
headings.insert(4,'Link')

df = pd.DataFrame(data=records,columns=headings[1:5],index=None)

print(df)

