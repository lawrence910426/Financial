import numpy as np
import pickle
import matplotlib.pyplot as plt

with open("Covariance.pickle", "rb") as handle:
    raw = pickle.load(handle)
    cov = raw["covariance"]

for row in raw["manifest"]:
    print(raw["manifest"][row])

pos = np.nan_to_num(np.clip(np.log(cov), -10, 10) + 10)
neg = np.nan_to_num(np.clip(np.log(-cov), -10, 10) - 10)
plt.imshow(pos + neg)
plt.colorbar()
plt.show()
