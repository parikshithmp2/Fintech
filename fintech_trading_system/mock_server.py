import asyncio
import websockets
import json
import random
from datetime import datetime

stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]

async def send_stock_data(websocket):
    while True:
        stock_data = []
        for stock in stocks:
            data = {
                "ticker": stock,
                "price": round(random.uniform(100, 2000), 2),
                "timestamp": datetime.utcnow().isoformat()
            }
            stock_data.append(data)
        await websocket.send(json.dumps(stock_data))
        await asyncio.sleep(5)  # simulate data every 5 seconds

async def main():
    async with websockets.serve(send_stock_data, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
