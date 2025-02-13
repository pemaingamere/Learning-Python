import ccxt
import time

exchange = ccxt.binance()

def get_bitcoin_price():
    ticker = exchange.fetch_ticker('BTC/USDT')
    price = ticker['last']
    return price

while True:
    try:
        price = get_bitcoin_price()
        print(f'Harga Bitcoin saat ini: ${price}')
        time.sleep(20)
    except Exception as e:
        print(f'Terjadi Kesalahan: {e}')
        break
