### Silhouette

# 1B
# 2C
# 3D
# 4A


### MNIST

from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

digits = load_digits()
X = digits.data
print(X.shape)
scaler = StandardScaler()
X = scaler.fit_transform(X)

tsne = TSNE(init="pca", n_components=2, perplexity=10, learning_rate="auto", random_state=0)
X = tsne.fit_transform(X)
print(X.shape)

plt.scatter(X[:, 0], X[:, 1], s=50)
model = KMeans(n_clusters=8, random_state=0)
labels = model.fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap="Set1")
centers = model.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c="orange", s=200, alpha=0.5)
plt.show()

print(silhouette_score(X, labels))
# vysledek mi vyšel 51 %

# Dobrovolný doplněk
# po původu dat jsem tentokrát pátrat nemusela, jedná se o velkou databázi ručně psaných číslic, v minulosti jsem ji už několikrát využila :-) Dobře se na ní trénuje, nicméně při práci s CNN mi tu vycházely výrazně lepší výsledky než na mém datasetu, neměla jsem tehdy tak pěná data jaká nabízí databáze
