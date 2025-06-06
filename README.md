# Fintech Price Monitor

A single-file Python project that simulates real-time stock price data using a WebSocket server and monitors price spikes over 2% within one minute.

# Requirements

- Python 3.7+
- Install dependencies:
  ```bash
  pip install websockets

# How to Use
# Start Mock WebSocket Server
bash
Copy
Edit
python fintech_price_monitor.py --mode server
# Start Client Monitor
bash
Copy
Edit
python fintech_price_monitor.py --mode client
# Alert Logic
The client receives price data every second.

It stores a rolling window of the last 60 seconds.

If the latest price is ≥ 2% higher than the price 60 seconds ago, an alert is triggered.

Example:
sql
Alert: Price increased by 2.15% in the last minute! Current price: 105.32

# Project Structure
fintech_trading_system/
├── app/
│   ├── __init__.py
│   ├── main.py        
│   ├── models.py
│   ├── database.py
│   ├── config.py
│   └── ...
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
├── mock_server.py # WebSocket server that streams simulated price data
├── price_monitor.py # WebSocket client that listens for price data and triggers alerts
├── requirements.txt # Dependencies list
└── README.md # Project guide
# Author
Parikshith
June 2025
