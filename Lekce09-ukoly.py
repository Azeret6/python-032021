### K Nearest Neighbors 1
import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import (accuracy_score, confusion_matrix, f1_score, precision_score, ConfusionMatrixDisplay)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/water-potability.csv")
open("water-potability.csv", 'wb').write(r.content)

data = pd.read_csv("water-potability.csv")
data.shape
data = data.dropna()
data.shape

X = data.drop(columns=["Potability"])
y = data["Potability"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

ks = [1, 3, 5, 7, 9, 11, 13, 15]
precision_scores = []

for k in ks:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    precision_scores.append(precision_score(y_test, y_pred))

plt.plot(ks, precision_scores)
plt.show()
print("Maximum: {0}, sousedů: {1}".format(max(precision_scores), (1+ 2*np.argmax(precision_scores))))



### K Nearest Neighbors 2

import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import (accuracy_score, confusion_matrix, f1_score, precision_score, ConfusionMatrixDisplay)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/kosatce.csv")
open("kosatce.csv", "wb").write(r.content)

data = pd.read_csv("kosatce.csv")

X = data.drop(columns=["target"])
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

ks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
f1_scores = []

for k in ks:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    f1_scores.append(f1_score(y_test, y_pred))

plt.plot(ks, f1_scores)
plt.show()
print("Maximum: {0}, sousedů: {1}".format(max(f1_scores), (1+ 2*np.argmax(f1_scores))))
# s použitím metody KNeighborsClassifier může metrika přesáhnout 85 %