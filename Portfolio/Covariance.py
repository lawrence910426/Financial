import csv
import numpy as np
import pickle

columns = ['當日均價(元)', '日期', '證券代碼', '簡稱']
col_index, data = [0 for _ in range(len(columns))], []

with open('../Samples/price.txt') as csvfile:
    rows = csv.reader(csvfile)
    located = False
    for row in rows:
        if located:
            data.append([row[col_index[i]] for i in range(len(columns))])
        else:
            for i in range(len(columns)):
                for j in range(len(row)):
                    if columns[i] == row[j]:
                        col_index[i] = j
            located = True

dates, ids, manifest =  {}, {}, {}
for item in data:
    manifest[len(ids)] = {"id": item[2], "name": item[3]}
    dates[item[1]] = dates[item[1]] if item[1] in dates else len(dates)
    ids[item[2]] = ids[item[2]] if item[2] in ids else len(ids)

price = [[-1 for _ in range(len(dates))] for _ in range(len(ids))]
for item in data:
    try:
        price[ids[item[2]]][dates[item[1]]] = float(item[0])
    except:
        pass

price_ans, manifest_ans = [], {}
for stock in range(len(ids)):
    total, amount = 0, 0
    for day in range(len(dates)):
        total += 0 if price[stock][day] == -1 else price[stock][day]
        amount += 0 if price[stock][day] == -1 else 1
    if amount != 0:
        ans = [total / amount if price[stock][i] == -1 else price[stock][i] for i in range(len(dates))]
        manifest_ans[len(price_ans)] = manifest[stock]
        price_ans.append(ans)

print(manifest_ans)
print(price_ans)

Covariance = np.cov(np.array(price_ans))
print(Covariance)

with open("Covariance.pickle", 'wb') as handle:
    pickle.dump({
        "price": price_ans,
        "manifest": manifest,
        "covariance": Covariance
    }, handle)
