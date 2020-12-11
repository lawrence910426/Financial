import pickle
import matplotlib.pyplot as plt
from functools import cmp_to_key
import numpy as np
import pandas as pd

with open('MinRiskPortfolio.pickle', 'rb') as handle:
    Risk, Portfolio = pickle.load(handle)

def compare(a, b):
    return b[0] - a[0]

Portfolio = sorted(Portfolio, key=cmp_to_key(compare))
Portfolio = [[item[0], item[1]["id"], item[1]["name"]] for item in Portfolio]

def Show(data):
    plt.bar(np.arange(len(data)), [item[0] for item in data])
    # plt.xticks(np.arange(len(data)), [item[2] for item in data])
    plt.show()

print("------ Top 30 -------")
print(pd.DataFrame(Portfolio[:30]))
print()
print("------ Last 30 -------")
print(pd.DataFrame(Portfolio[-30:]))
Show(Portfolio)
