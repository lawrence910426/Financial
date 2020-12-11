import numpy as np
import pickle
import matplotlib.pyplot as plt

with open("Covariance.pickle", "rb") as handle:
    raw = pickle.load(handle)
    cov = raw["covariance"]

for row in raw["manifest"]:
    print(raw["manifest"][row])

cov = np.clip(np.nan_to_num(np.log(cov)), -10, 10)
plt.imshow(cov)
plt.colorbar()
plt.show()
