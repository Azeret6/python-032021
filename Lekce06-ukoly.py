### Pšenice

import requests
from scipy.stats import mannwhitneyu
import  pandas as pd

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/psenice.csv") as r:
  open("psenice.csv", 'w', encoding="utf-8").write(r.text)

psenice = pd.read_csv("psenice.csv")
print(psenice.head())
psenice.shape

# H0: Průměrná délka zrn obou odrůd je stejná
# H1: Průměrná délka zrn obou odrůd je různá

psenice["Rosa"]
mannwhitneyu(psenice["Rosa"], psenice["Canadian"])
# výsledek je p-value = 3.522437521029982e-24 (hodně pod hladinou významnosti 0.05)
# nulovou hypotézu zamítáme -> průměrná délka zrn obou odrůd není stejná



### Jemné částice 2
import requests
from scipy.stats import mannwhitneyu
import pandas as pd

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

pd.set_option('display.max_columns', None)
znecisteni = pd.read_csv("air_polution_ukol.csv")
znecisteni.head()
znecisteni["date"] = pd.to_datetime(znecisteni["date"])
znecisteni["rok"] = znecisteni["date"].dt.year
znecisteni["mesic"] = znecisteni["date"].dt.month

znecisteni2019 = znecisteni[(znecisteni["rok"] == 2019) & (znecisteni["mesic"] == 1)]
znecisteni2020 = znecisteni[(znecisteni["rok"] == 2020) & (znecisteni["mesic"] == 1)]

# H0: Znečištění (dáno množstvím částic ve vzduchu) bylo v obou letech stejné
# H1: Znečištění (dáno množstvím částic ve vzduchu) se v letech 2019 a 2020 lišilo

mannwhitneyu(znecisteni2019["pm25"], znecisteni2020["pm25"])
# Výsledná p-hodnota je 1.17 %, tudíž můžeme zamítnout nulovou hypotézu říkající, že množství jemných částic ve vzduchu bylo stejné.
# Přijímáme alternativní hypotézu, která nám říká, že množství částic se v obou letech lišilo.