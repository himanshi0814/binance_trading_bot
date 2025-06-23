print("✅ Script started")

import logging
import time
import os
from dotenv import load_dotenv
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException

# ✅ Load API keys from .env
load_dotenv()
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

class BasicBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)

        # ✅ Point client to Binance Futures Testnet
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
        self.client.API_URL = "https://testnet.binancefuture.com"

        # ✅ Set time sync before placing any request
        try:
            server_time = self.client._request("get", "fapi/v1/time", False)
            local_time = int(time.time() * 1000)
            self.client.time_offset = server_time['serverTime'] - local_time
            self.client._get_timestamp = lambda: int(time.time() * 1000 + self.client.time_offset)
        except Exception as e:
            print("❌ Failed to sync time:", str(e))
            exit()

        logging.basicConfig(level=logging.INFO)

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            return order
        except BinanceAPIException as e:
            logging.error(f"Binance API error: {e.message}")
            return {"error": f"BinanceAPIException(code={e.code}): {e.message}"}
        except Exception as e:
            logging.exception("Unexpected error")
            return {"error": str(e)}

if __name__ == "__main__":
    print("Welcome to Binance Futures Trading Bot (Testnet)")

    bot = BasicBot(api_key, api_secret)

    while True:
        symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
        side = input("Order side (buy/sell): ").lower()
        order_type = input("Order type (market/limit): ").lower()
        quantity = float(input("Quantity: "))

        if order_type == "market":
            result = bot.place_market_order(symbol, side, quantity)
        else:
            result = {"error": "Only market orders are implemented."}

        print("Order Response:")
        print(result)

