### Titanic
import requests
import pandas as pd
import numpy as np

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/titanic.csv")
open("titanic.csv", 'wb').write(r.content)

titanic = pd.read_csv("titanic.csv")
print(titanic.head().to_string()) # podívám se, jak tabulka vypadá

# kontingenční tabulka porovnávající závislost mezi pohlavím cestujícího, třídou ve které cestoval a tím, jestli přežil potopeí Titanicu
titanic_pivot = pd.pivot_table(titanic, index="Sex", columns="Pclass", values="Survived", aggfunc=np.sum)
print(titanic_pivot.head())

# druhá možnost - přes groupby
titanic_grouped = titanic.groupby(["Pclass", "Sex"]).sum("Survived")
print(titanic_grouped.head(6))


### Pujcovani kol
import requests
import pandas as pd
import numpy as np

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/london_merged.csv")
open("london_merged.csv", 'wb').write(r.content)

london = pd.read_csv("london_merged.csv")
print(london.head().to_string()) # podívám se, jak tabulka vypadá

london["date"] = pd.to_datetime(london["timestamp"]) # přidám sloupec s požadovaným typem
london["year"] = london["date"].dt.year # přidám sloupec s rokem
print(london.head().to_string()) # zkontroluji správnost sloupců

# kontingenční tabulka porovnávající kód počasí se sloupcem udávajícím rok
london_pivot = pd.pivot_table(london, index="weather_code", columns="year", values="cnt", fill_value=0, aggfunc=np.sum)
print(london_pivot.head())