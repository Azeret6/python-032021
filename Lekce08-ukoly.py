### Cena akcie
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.graphics.tsaplots import plot_acf

pd.set_option('display.max_columns', None)
data = yf.Ticker("CSCO")
data_csco = data.history(period="5y")
print(data_csco.head())
print(data_csco["Close"].autocorr(lag=1))
plot_acf(data_csco["Close"])
plt.show()

mod = AutoReg(data_csco["Close"], lags=5, trend="t", seasonal=False)
res = mod.fit()

predictions = res.predict(start=data_csco.shape[0], end=data_csco.shape[0] + 5)
data_forecast = pd.DataFrame(predictions, columns=["Close_prediction"])
data_with_prediction = pd.concat([data_csco, data_forecast])
data_with_prediction[["Close", "Close_prediction"]].tail(50).plot()

print(data_with_prediction["Close"])
plt.show()



## Otázky na Python
import requests
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/MLTollsStackOverflow.csv")
open("MLTollsStackOverflow.csv", "wb").write(r.content)

data = pd.read_csv("MLTollsStackOverflow.csv")

decompose = seasonal_decompose(data["python"], model='multiplicative', period=12)
decompose.plot()
plt.show()

mod = ExponentialSmoothing(data["python"], seasonal_periods=12, trend="multiplicative", seasonal="multiplicative", initialization_method="estimated")
res = mod.fit()
data["HM"] = res.fittedvalues
data_forecast = pd.DataFrame(res.forecast(12), columns=["Forecast"])
data_with_forecast = pd.concat([data, data_forecast])
data_with_forecast[["HM", "python", "Forecast"]].plot()
plt.show()