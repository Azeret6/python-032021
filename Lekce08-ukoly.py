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
data_with_prediction = pd.concat([data_cisco, data_forecast])
data_with_prediction[["Close", "Close_prediction"]].tail(50).plot()

print(data_with_prediction["Close"])
plt.show()

### Otázky na Python