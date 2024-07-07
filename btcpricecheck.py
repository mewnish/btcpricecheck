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
    last_price = None
    green_count = 0
    red_count = 0
    while True:
        price = get_btc_price()
        if price is not None:
            if last_price is not None:
                if price > last_price:
                    print(f"\033[92mThe current price of BTC is ${price}\033[0m")  # Green text
                    green_count += 1
                elif price < last_price:
                    print(f"\033[91mThe current price of BTC is ${price}\033[0m")  # Red text
                    red_count += 1
                else:
                    print(f"The current price of BTC is ${price}")  # No color if unchanged
            else:
                print(f"The current price of BTC is ${price}")  # No color for the first fetch
            last_price = price
        else:
            print("Failed to retrieve BTC price.")
        
        # Print color totals
        print(f"\033[92mGreen total: {green_count}\033[0m, \033[91mRed total: {red_count}\033[0m")
        
        # Wait for 3 minutes (180 seconds) before checking again
        time.sleep(180)

if __name__ == "__main__":
    report_btc_price()
