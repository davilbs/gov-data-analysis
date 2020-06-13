import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt(fname="importacoes-gas-natural/importacao/importacao-gas-natural-2000-2020-m3.csv",
                     delimiter=";", usecols=(4,9), encoding="utf-8", skip_header=1)

print(data)