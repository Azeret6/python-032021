### Lexikon zvířat 1
import requests
import pandas as pd

pd.set_option('display.max_columns', None)
r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)
lexikon = pd.read_csv("lexikon-zvirat.csv", sep=";").dropna(how="all", axis=0).dropna(how="all", axis=1)
print(lexikon.head())
print(lexikon.shape)

# funkce kontrolující, zda je odkaz sestaven podel pravidel:
def check_url(radek):
  if isinstance(radek.image_src, str) == False:
    src = str(radek.image_src)
    image_err = radek.title+" : "+src
  elif radek.image_src.startswith("https://zoopraha.cz/images/") == False:
    image_err = radek.title+" : "+radek.image_src
  elif (radek.image_src.endswith("jpg")|radek.image_src.endswith("JPG")) == False:
    image_err = radek.title+" : "+radek.image_src
  else:
    image_err = "no_err"
  return image_err

# zkontrolujeme celou tabulku:
pocet = 0
for radek in lexikon.itertuples():
    image_err = check_url(radek)
    if image_err != "no_err":
        pocet += 1
        print(image_err)
print(f"Počet zvířat se špatnou url je: {pocet}")

### Lexikon zvířat 2
import requests
import pandas as pd

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)
lexikon = pd.read_csv("lexikon-zvirat.csv", sep=";").dropna(how="all", axis=0).dropna(how="all", axis=1)
print(lexikon.head())
print(lexikon.shape)

# funkce popisek
def popisek(radek):
    text = "{0} preferuje následující typ stravy: {1}. ".format(radek.title, radek.food)
    text += "Konkrétně ocení když mu do misky přistanou {0}. \nJak toto zvíře poznáme: {1}".format(radek.food_note, radek.description)
    return text

lexikon["popisek"] = lexikon.apply(popisek, axis=1)

# Vyzkoušíme pro naše dva modelové texty:
print(lexikon["popisek"][320])
print(lexikon["popisek"][300])

