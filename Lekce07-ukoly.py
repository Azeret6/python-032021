### Kvalita cementu

import requests
import pandas as pd
import statsmodels.formula.api as smf
import seaborn
import matplotlib.pyplot as plt

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Concrete_Data_Yeh.csv")
open("Concrete_Data_Yeh.csv", 'w', encoding="utf-8").write(r.text)

cement = pd.read_csv("Concrete_Data_Yeh.csv")
pd.set_option('display.max_columns', None)
print(cement.head())

seaborn.heatmap(cement.corr())
plt.show()

mod = smf.ols(formula="csMPa ~ cement + slag + flyash + water + superplasticizer + coarseaggregate + fineaggregate + age", data=cement)
res = mod.fit()
print(res.summary())
# koeficient determinace je 0.616, což není zrovna moc. Záporný regresní koeficient má voda, zkusím vytvořit nový model, ve kterém nebude voda zahrnuta:
mod = smf.ols(formula="csMPa ~ cement + slag + flyash + superplasticizer + coarseaggregate + fineaggregate + age", data=cement)
res = mod.fit()
print(res.summary())
# koeficient determinace klesl na 0.610, voda měla na model minimální vliv



### Ryby
import requests
import pandas as pd
import statsmodels.formula.api as smf
import seaborn
import matplotlib.pyplot as plt

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Fish.csv")
open("Fish.csv", 'w', encoding="utf-8").write(r.text)

ryby = pd.read_csv("Fish.csv")
pd.set_option('display.max_columns', None)
print(ryby.head())

mod = smf.ols(formula="Weight ~ Length2", data=ryby)
res = mod.fit()
print(res.summary())
# přesnost modelu je 84.4 %

mod = smf.ols(formula="Weight ~ Length2 + Height", data=ryby)
res = mod.fit()
print(res.summary())
# přesnost modelu s přidáním informace o délce ryb je 87,5 %

druh_ryb = ryby.groupby('Species')['Weight'].mean()
ryby['prumerna_vaha'] = ryby['Species'].map(druh_ryb)
mod = smf.ols(formula="Weight ~ Length2 + Height + prumerna_vaha", data=ryby)
res = mod.fit()
print(res.summary())
# přesnost modelu je nyní 90 %
