import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd
import pickle
import time

ans = {}

def Crawl(corp_id, year, season):
    report_url = f"https://mops.twse.com.tw/server-java/t164sb01?step=1&CO_ID={corp_id}&SYEAR={year}&SSEASON={season}&REPORT_ID=C"
    print(f"cid {corp_id}, yr {year}, season {season}")
    with req.urlopen(report_url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        for table in soup.find_all('table'):
            try:
                name = table.find_all('tr')[0].find('th').text
                if sum(1 if item in name else 0 for item in ['Cash', 'Income', 'Balance']) == 0:
                    continue
                columns = [th.text for th in table.find_all('tr')[1].find_all('th')]
                rows = []
                for tr in table.find_all('tr')[1:]:
                    rows.append([td.text for td in tr.find_all('td')])
                ans[(corp_id, year, season, name)] = (columns, rows)
                print(f"Corp -> {corp_id}, Year -> {year}, Season -> {season}, Name -> {name}")
            except:
                continue



for corp_id in range(1000, 10000):
    for year in range(2000, 2021):
        for season in range(1, 5):
            time.sleep(1)
            Crawl(corp_id, year, season)        

with open('report.pickle', 'wb') as handle:
    pickle.dump(ans, handle, protocol=pickle.HIGHEST_PROTOCOL)

# for index in ans:
#     print(index, ans[index])


# price_url = f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={date}&stockNo={corp_id}"
