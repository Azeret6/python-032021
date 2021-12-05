### Dřeviny

import pandas as pd
import numpy as np
from sqlalchemy import create_engine, inspect
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432

USER = "tb.bohata"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = ".5BnGvpyFHQCL4sJ"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
inspector = inspect(engine)

# tabulka smrk se sloupcem dd_txt odpovídajícím textu 'Smrk, jedle, douglaska'
smrk = pd.read_sql("SELECT * FROM dreviny WHERE dd_txt='Smrk, jedle, douglaska'", con=engine)
print(smrk.head())

# tabulka nahodila_tezba se sloupcem druhtez_txt odpovídajícím textu 'Nahodilá těžba dřeva'
nahodila_tezba = pd.read_sql("SELECT * FROM dreviny WHERE druhtez_txt ='Nahodilá těžba dřeva'", con=engine)
print(nahodila_tezba.head())

# graf vývoje objemu těžby za rok
smrk.sort_values(by="rok").plot.bar(x="rok", y="hodnota", title="Tezba smrk, jedle, douglaska")
print(smrk[["rok", "hodnota"]]) # ciselne vyjadreni k vizualni kontrole

# vývoj objemu v čase pomocí pivot + grafické znázornění
pivot_tezba = pd.pivot_table(nahodila_tezba, values="hodnota", index="rok", columns="prictez_txt", aggfunc=np.sum)
pivot_tezba.plot.bar(legend=True, title="Priciny tezby")
plt.show()
print(pivot_tezba.head()) # ciselne vyjadreni k vizualni kontrole


### Chicago Crime
import pandas as pd
from sqlalchemy import create_engine, inspect

pd.set_option('display.max_columns', None)

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432

USER = "tb.bohata"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = ".5BnGvpyFHQCL4sJ"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

kradeze = pd.read_sql("SELECT * FROM crime WHERE \"PRIMARY_DESCRIPTION\" = 'MOTOR VEHICLE THEFT'", con=engine) # vyfiltrujeme si motorová vozidla
kradeze = kradeze[kradeze["SECONDARY_DESCRIPTION"] == "AUTOMOBILE"] # vyfiltrujeme si pouze automobily
kradeze = kradeze[["CASE#", "DATE_OF_OCCURRENCE"]] # potřebujeme znát počet případů a měsíc

kradeze["DATE_OF_OCCURRENCE"] = pd.to_datetime(kradeze["DATE_OF_OCCURRENCE"]) # převedeme na datum
kradeze["month"] = kradeze["DATE_OF_OCCURRENCE"].dt.month # dále nás bude zajímat měsíc, ten si dáme do speciálního odtsavce
print(kradeze.head())

# zjistíme počty pro jednotlivé měsíce
kradeze_mesicni = kradeze.groupby("month").size()
kradeze_mesicni.plot.bar(x="month", y="counts", legend=True)
plt.show()
print(kradeze_mesicni) # ciselne vyjadreni k vizualni kontrole

