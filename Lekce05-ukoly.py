### Kryptoměny

import requests
import seaborn
import pandas as pd
import matplotlib.pyplot as plt

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)
pd.set_option('display.max_columns', None)

krypto = pd.read_csv("crypto_prices.csv")
print(krypto.head())

# zavírací cena vyjádřená v procentech
krypto["zmena_procenta"] = krypto.groupby(["Name"]).shift(-1)["Close"].pct_change()

# korelační matice změn
krypto_pivot = krypto.pivot('Date','Name','zmena_procenta').reset_index()
# krypto_pivot.to_csv('krypto.csv', index=True, sep=';')
# np.savetxt('data.csv', krypto_pivot, delimiter=';')
krypto_pivot = krypto_pivot.corr()
print(krypto_pivot.head())

# for cyklus k vyhledání nejvíce a nejméně korelovaných
maximum = 0
minimum = 1
znamenko = 1
index_radky_max = 0
index_sloupce_max = 0
index_radky_min = 0
index_sloupce_min = 0
for i in range(krypto_pivot.shape[0]):
    for j in range(krypto_pivot.shape[1]):
        if i < j:
            if krypto_pivot.iloc[i, j] > maximum:
                maximum = krypto_pivot.iloc[i, j]
                index_radky_max = i
                index_sloupce_max = j
            elif abs(krypto_pivot.iloc[i, j]) < minimum:
                minimum = abs(krypto_pivot.iloc[i, j])
                index_radky_min = i
                index_sloupce_min = j
                if minimum < 0:
                    znamenko = -1


print("Maximální korelace je:", maximum, "s indexy", index_radky_max, "a", index_sloupce_max)
print("Minimální korelace je:", minimum*znamenko, "s indexy", index_radky_min, "a", index_sloupce_min)

{krypto_pivot.columns.get_loc(c): c for idx, c in enumerate(krypto_pivot.columns)}

krypto_max = krypto_pivot.loc[:, [krypto_pivot.columns[index_radky_max], krypto_pivot.columns[index_sloupce_max]]]
krypto_min = krypto_pivot.loc[:, [krypto_pivot.columns[index_radky_min], krypto_pivot.columns[index_sloupce_min]]]
krypto_max = krypto_max.astype(float)
krypto_min = krypto_min.astype(float)
{krypto_max.columns.get_loc(c): c for idx, c in enumerate(krypto_max.columns)}
{krypto_min.columns.get_loc(c): c for idx, c in enumerate(krypto_min.columns)}

# grafy
seaborn.jointplot(krypto_max.columns[0], krypto_max.columns[1], krypto_max.dropna(), kind='scatter', color='red') # nejvíce korelované měny
plt.show()
seaborn.jointplot(krypto_min.columns[0], krypto_min.columns[1], krypto_min.dropna(), kind='scatter', color='green') # nejméně korelované měny
plt.show()



### Tempo růstu
import requests
import statistics
import pandas as pd

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)
pd.set_option('display.max_columns', None)

krypto = pd.read_csv("crypto_prices.csv")
krypto = krypto.loc[krypto["Name"] == "Monero"] # vybereme Monero, ať můžeme porovnat s ukázkovým příkladem
krypto = krypto["Close"].pct_change() + 1
krypto_seznam = krypto.tolist()[1:]

print(statistics.geometric_mean(krypto_seznam))
print("Průměrný mezidenní růst pro Monero je", statistics.geometric_mean(krypto_seznam)-1)


