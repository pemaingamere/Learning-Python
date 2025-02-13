import os
from dotenv import load_dotenv
import ccxt
import time

# Load file api.env
load_dotenv(dotenv_path='fire.env')

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

exchange = ccxt.bybit({
    'apiKey': api_key,
    'secret': api_secret,
})

def get_bitcoin_price():
    try:
        # Mengambil harga terbaru untuk BTC/USDT
        ticker = exchange.fetch_ticker('BTC/USDT')
        price = ticker['last']
        return price
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return None

while True:
    try:
        price = get_bitcoin_price()
        if price:
            print(f'Harga Bitcoin saat ini: ${price}')
        time.sleep(20)
    except Exception as e:
        print(f'Terjadi Kesalahan: {e}')
        break