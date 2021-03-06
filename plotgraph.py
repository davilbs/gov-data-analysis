import numpy as np
import matplotlib.pyplot as plt
from scypy import stats

years = np.genfromtxt(fname="importacoes-gas-natural/importacao/importacao-gas-natural-2000-2020-m3.csv",
                     dtype="int", delimiter=";", usecols=(0), encoding="utf-8", skip_header=1)

months = np.genfromtxt(fname="importacoes-gas-natural/importacao/importacao-gas-natural-2000-2020-m3.csv",
                     dtype="str", delimiter=";", usecols=(4,5,6,7,8,9,10,11,12,13,14,15), encoding="utf-8", max_rows=1)

data = np.genfromtxt(fname="importacoes-gas-natural/importacao/importacao-gas-natural-2000-2020-m3.csv",
                     delimiter=";", usecols=(4,5,6,7,8,9,10,11,12,13,14,15), encoding="utf-8", skip_header=1)

for month in range(len(months)):
    plt.scatter(years, [monthdata[month] for monthdata in data], label=months[month])
plt.legend(loc="upper right", ncol=3)
plt.show()
