import requests
from server.config import Config
from datetime import datetime

def fetch_stock_data(ticker):
    """Fetches the latest stock data for a given ticker symbol."""
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": ticker,
        "interval": "5min",
        "apikey": Config.ALPHA_VANTAGE_API_KEY,
    }

    # Make the API request
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Error fetching stock data: {response.status_code}, {response.text}")

    # Parse the JSON response
    data = response.json()
    if "Time Series (5min)" not in data:
        raise Exception(f"Unexpected response format: {data}")

    # Extract the latest entry from the time series data
    time_series = data["Time Series (5min)"]
    latest_time = sorted(time_series.keys())[-1]
    latest_data = time_series[latest_time]

    # Map and return the formatted data
    return {
        "ticker": ticker,
        "timestamp": datetime.strptime(latest_time, "%Y-%m-%d %H:%M:%S"),  # Convert string to datetime
        "open_price": float(latest_data["1. open"]),  # Updated key
        "high_price": float(latest_data["2. high"]),  # Updated key
        "low_price": float(latest_data["3. low"]),   # Updated key
        "close_price": float(latest_data["4. close"]), # Updated key
        "volume": int(latest_data["5. volume"]),
    }