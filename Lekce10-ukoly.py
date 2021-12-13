### Feature Importance

import requests
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split


r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/soybean-2-rot.csv")
open("soybean-2-rot.csv", "wb").write(r.content)

data = pd.read_csv("soybean-2-rot.csv")

X = data.drop(columns=["class"])
input_features = X.columns

y = data["class"]

oh_encoder = OneHotEncoder()
X = oh_encoder.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=0)

clf = DecisionTreeClassifier(max_depth=3, min_samples_leaf=1)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(f1_score(y_test, y_pred, average="weighted"))
# f1_score je 0.93
print(clf.feature_importances_)
print(oh_encoder.feature_names_in_)
# největší důležitost má proměnná "plant-stand", má hodnotu 52.35 %
# rozdíl mezi použití pouze jedné proměnné a všech proměnných je poměrně dost velký, pro úspěšnou klasifikaci potřebujeme použít všechny



### Auto

import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/auto.csv")
open("auto.csv", "wb").write(r.content)

data = pd.read_csv("auto.csv", na_values=["?"])
pd.set_option('display.max_columns', None)
print(data.head())
print(data.shape)
data = data.dropna() # zbavíme se neznámých/prázdných hodnot
print(data.shape)
# sloupec origin: 1=USA, 2=Evropa, 3=Japonsko

df_pivot = pd.pivot_table(data, index = "year", columns="origin", values="mpg", aggfunc=numpy.mean, margins = True)
print(df_pivot)
df_pivot.plot()
plt.show()

X = data.drop(columns=["origin", "name"])
y = data["origin"]

encoder_x = OneHotEncoder()
X = encoder_x.fit_transform(X)
encoder_y = LabelEncoder()
y = encoder_y.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

scaler = StandardScaler(with_mean=False)
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = DecisionTreeClassifier(random_state=0)

clf = GridSearchCV(model, param_grid={'max_depth': [3, 5, 7, 9, 11, 13], 'min_samples_leaf': [1, 3, 5]})
clf.fit(X_train, y_train)

print(clf.best_params_)
# {'max_depth': 13, 'min_samples_leaf': 1}
print(round(clf.best_score_, 2))
# 0.78
y_pred = clf.predict(X_test)
print(f1_score(y_test, y_pred, average='micro'))
# 0.788135593220339