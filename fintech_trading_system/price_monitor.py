import asyncio
import websockets
import json
from datetime import datetime, timedelta

stock_prices = {}

async def monitor_stock_prices():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            data = await websocket.recv()
            prices = json.loads(data)

            current_time = datetime.utcnow()

            for stock in prices:
                ticker = stock["ticker"]
                price = stock["price"]

                # Save price history
                if ticker not in stock_prices:
                    stock_prices[ticker] = []

                stock_prices[ticker].append((current_time, price))

                # Remove old prices (older than 1 min)
                stock_prices[ticker] = [
                    (t, p) for (t, p) in stock_prices[ticker]
                    if t > current_time - timedelta(minutes=1)
                ]

                if len(stock_prices[ticker]) >= 2:
                    old_price = stock_prices[ticker][0][1]
                    percent_change = ((price - old_price) / old_price) * 100
                    if percent_change > 2:
                        print(f"[ALERT] {ticker} ↑ {percent_change:.2f}% in 1 minute!")

            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(monitor_stock_prices())
