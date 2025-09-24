# filename: stock_price_chart.py
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical stock price data for META and TESLA
meta_data = yf.Ticker("META").history(period="1y")  # 1 year historical data for META
tesla_data = yf.Ticker("TSLA").history(period="1y")  # 1 year historical data for TESLA

# Prepare the data for plotting
meta_dates = meta_data.index
meta_prices = meta_data['Close']

tesla_dates = tesla_data.index
tesla_prices = tesla_data['Close']

# Plot the stock price change chart
plt.figure(figsize=(12, 6))
plt.plot(meta_dates, meta_prices, label='META')
plt.plot(tesla_dates, tesla_prices, label='TESLA')
plt.title('META vs TESLA Stock Price Change')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.show()