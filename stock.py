import yfinance as yf
data = yf.download("TSLA", period="1mo")
print(type(data))
print(data.close)

x = 25
y = 50


