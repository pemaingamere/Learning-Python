import os
from dotenv import load_dotenv
import requests
import time

# Load API key dan secret
load_dotenv(dotenv_path='fire.env')

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

# Fungsi untuk mengambil harga Bitcoin
def get_bitcoin_price():
    url = 'https://api.bybit.com/v2/public/tickers?symbol=BTCUSDT'
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200 and data.get('result'):
            price = data['result'][0]['last_price']
            return price
        else:
            print("Gagal mengambil data harga.")
            return None
    except Exception as e:
        print(f"Terjadi kesalahan saat mengambil data: {e}")
        return None

while True:
    try:
        price = get_bitcoin_price()
        if price:
            print(f'Harga Bitcoin saat ini: ${price}')
        time.sleep(20)  # Tunggu selama 20 detik sebelum mengambil harga lagi
    except Exception as e:
        print(f'Terjadi Kesalahan: {e}')
        break
