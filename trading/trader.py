import os
import pandas as pd
import numpy as np
import joblib
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, timedelta, timezone
from logger import log_message
from dotenv import load_dotenv

load_dotenv()

# Load API keys
ALPACA_API_KEY = os.getenv("ALPACA_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET")

# Alpaca clients
trading_client = TradingClient(ALPACA_API_KEY, ALPACA_SECRET_KEY, paper=True)
data_client = StockHistoricalDataClient(ALPACA_API_KEY, ALPACA_SECRET_KEY)

# Load model
model = joblib.load("../notebooks/stock_trading_model.pkl")

# 1) Fetch latest AAPL data
end_date = datetime.now(timezone.utc)
start_date = end_date - timedelta(days=40)

request = StockBarsRequest(
    symbol_or_symbols=["AAPL"],
    timeframe=TimeFrame.Day,
    start=start_date.isoformat(),
    end=end_date.isoformat(),
    feed="iex"
)

bars = data_client.get_stock_bars(request)
df = bars.df
df = df.reset_index()
df = df[['timestamp','open','high','low','close','volume']]
df = df.rename(columns={'timestamp':'Date'})
df.set_index('Date', inplace=True)

# 2) Feature engineering
df['Return'] = df['close'].pct_change()
df['MA5'] = df['close'].rolling(5).mean()
df['MA10'] = df['close'].rolling(10).mean()
df['MA20'] = df['close'].rolling(20).mean()
df['Prev_Close'] = df['close'].shift(1)
df['Prev_Return'] = df['Return'].shift(1)
df = df.dropna()

# Use last row
X_today = df.iloc[-1:][[
    'open','high','low','close','volume',
    'Return','MA5','MA10','MA20',
    'Prev_Close','Prev_Return'
]]

# 3) Predict
prediction = model.predict(X_today)[0]  # 1=up, 0=down
QTY = 1

# --- NEW: check current position ---
positions = trading_client.get_all_positions()
aapl_position = next((p for p in positions if p.symbol == "AAPL"), None)
current_qty = int(aapl_position.qty) if aapl_position else 0

# 4) Trading logic
if prediction == 1:
    # BUY signal
    log_message(f"Buying {QTY} share(s)")
    side = OrderSide.BUY

    order = MarketOrderRequest(
        symbol="AAPL",
        qty=QTY,
        side=side,
        time_in_force=TimeInForce.DAY
    )
    response = trading_client.submit_order(order)
    print(response)

else:
    # SELL signal — only if you hold shares
    if current_qty >= QTY:
        log_message(f"Selling {QTY} share(s) (Current holdings: {current_qty})")
        side = OrderSide.SELL

        order = MarketOrderRequest(
            symbol="AAPL",
            qty=QTY,
            side=side,
            time_in_force=TimeInForce.DAY
        )
        response = trading_client.submit_order(order)
        print(response)
    else:
        log_message(f"Sell signal detected, but you own 0 shares — skipping sell order.")
