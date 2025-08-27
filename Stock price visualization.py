import yfinance as yf
import matplotlib.pyplot as plt

# Download stock data (Apple as example)
stock = yf.download("AAPL", start="2024-01-01", end="2024-08-01")

# Print summary
print(stock.head())

# Plot closing prices
stock["Close"].plot(title="Apple Stock Price (2024)", figsize=(10,5))
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.show()
