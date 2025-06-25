🟢 Binance Futures Trading Bot (Testnet)

This is a simple Python-based trading bot that connects to the **Binance Futures Testnet** using your API credentials. It allows you to place market buy/sell orders directly from the command line.

🚀 Features

- ✅ Connects securely to Binance Testnet
- ✅ Places market orders (buy/sell)
- ✅ Supports `.env` for secure API key handling
- ✅ Syncs system time with Binance server
- ✅ Handles API errors gracefully

 📁 Folder Structure
 
binance-trading-bot/

├── .env # Stores your Binance API credentials

├── .gitignore # Prevents sensitive/log files from being committed

├── README.md # This file

├── requirements.txt # List of dependencies

├── trading_bot.py # Main Python bot script

└── trading_bot.log # Log file (auto-generated)

:Setup Instructions

1. Clone the Repository
   
git clone https://github.com/himanshi0814/binance_trading_bot.git

cd binance_trading_bot

2. Install Dependencies
   
pip install -r requirements.txt
If you encounter issues with python-binance, install from source:

pip install git+https://github.com/sammchardy/python-binance.git@master

3. Create a .env File

Inside the project folder, create a .env file with your Binance Testnet credentials:

API_KEY=your_testnet_api_key

API_SECRET=your_testnet_api_secret

🚨 Never share your .env file publicly!

4. Run the Bot
   
python trading_bot.py

: Example Usage

✅ Script started

Welcome to Binance Futures Trading Bot (Testnet)

Enter trading pair (e.g., BTCUSDT): BTCUSDT

Order side (buy/sell): buy

Order type (market/limit): market

Quantity: 0.01

Order Response:
{...}

📌Important points:

-This bot only places market orders on the Binance Futures Testnet.

-Use it for educational or testing purposes only — not for real-money trading.

-If needed, extend the bot to support stop-loss, limit orders, or indicators.

🛡️ License

This project is open-source and available under the MIT License.

 Author
Created by Himanshi Rajput

 GitHub: @himanshi0814










