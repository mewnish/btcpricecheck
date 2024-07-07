import requests
import time

def get_btc_price():
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        response.raise_for_status()
        data = response.json()
        return data['bitcoin']['usd']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching BTC price: {e}")
        return None

def report_btc_price():
    while True:
        price = get_btc_price()
        if price is not None:
            print(f"The current price of BTC is ${price}")
        else:
            print("Failed to retrieve BTC price.")
        
        # Wait for 3 minutes (180 seconds) before checking again
        time.sleep(180)

if __name__ == "__main__":
    report_btc_price()
