### Swing states
import requests
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
  open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)
prezidenti = pd.read_csv("1976-2020-president.csv")
prezidenti.head()

prezidenti_sorted = prezidenti.sort_values(by=["year", "state", "candidatevotes"], ascending = False)
prezidenti_sorted["rank"] = prezidenti_sorted.groupby(["year", "state"])["candidatevotes"].rank(method="min", ascending = False)

# ponecháme pouze vítěze:
prezidenti_vitezove = prezidenti_sorted[prezidenti_sorted["rank"] == 1]

# přidáme sloupec indikující opakované vítězství:
prezidenti_vitezove = prezidenti_vitezove.sort_values(by=["state", "year"])
prezidenti_vitezove["vitez_dvakrat"] = prezidenti_vitezove.groupby(["state"])["party_simplified"].shift(-1)
print(prezidenti_vitezove.head())

# přidáme sloupec oznamující, zda došlo minulé dva roky ke změně
prezidenti_vitezove = prezidenti_vitezove.dropna(subset=["vitez_dvakrat"])
prezidenti_vitezove["zmena_vitezstvi"] = np.where(prezidenti_vitezove["party_simplified"] == prezidenti_vitezove["vitez_dvakrat"],0,1)

# agregace
staty_zmeny = pd.DataFrame(prezidenti_vitezove.groupby(["state"])["zmena_vitezstvi"].sum())
staty_zmeny = staty_zmeny.sort_values(by = ["zmena_vitezstvi"])
print(staty_zmeny)



import requests
import pandas
import numpy
with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
    open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)



# Pomocí shift přidám sloupec s vítězem následujících voleb:
president1_sorted["party_detailed_next"] = president1_sorted["party_detailed"].shift(periods=-1)
# Vyhodím rok 2020:
president1_sorted = president1_sorted[president1_sorted["year"] != 2020]
# Dodám sloupec changed, hodnota 1 = změna vítěze:
president1_sorted["changed"] = numpy.where(president1_sorted["party_detailed"] != president1_sorted["party_detailed_next"], 1, 0)
# Kontrolní výpis - Florida, 5x změna, což se potvrdí i pak níže ve výsledku
president_Florida = president1_sorted[(president1_sorted["state"] == "FLORIDA")]
print("KONTROLA - Počet změn vítěze voleb zaznamenané ve sloupci changed pro stát FLORIDA")
print(president_Florida[["state", "year", "party_detailed", "party_detailed_next", "changed"]])
print()

# Seskupím podle států a posčítám v rámci nich změny, seřadím od nejvíc "swinging":
president1_final = president1_sorted.groupby(["state"]).sum("changed")
president1_final = president1_final.sort_values(["changed"], ascending=False)
print("VÝSLEDEK - Státy, kde se nejvíc střídaly vítězné strany - počet změn = changed:")
print(president1_final[["changed"]])
print()


### Jemné částice
import requests
import pandas as pd

pd.set_option('display.max_columns', None)
with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)
znecisteni = pd.read_csv("air_polution_ukol.csv")
znecisteni.head()
znecisteni["date"] = pd.to_datetime(znecisteni["date"])
znecisteni["rok"] = znecisteni["date"].dt.year
znecisteni["mesic"] = znecisteni["date"].dt.month

# pivot tabulka s průměrným počtem jemných částic v jednotlivých měsících a jednotlivých letech
znecisteni_pivot = pd.pivot_table(znecisteni, index = "rok", columns="mesic", values= "pm25", aggfunc="mean", margins = True)
print(znecisteni_pivot)

# bonus - teplotní mapa
import seaborn as sns
sns.heatmap(znecisteni_pivot, annot=True, fmt=".1f")
plt.show()
