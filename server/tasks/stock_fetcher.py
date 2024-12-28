import random
from datetime import datetime

def fetch_stock_data(ticker):
    # Mock data generation
    return {
        "ticker": ticker,
        "price": round(random.uniform(50, 150), 2),
        "volume": random.randint(1000, 1000000),
        "timestamp": datetime.utcnow()
    }