import requests


def get_binance_prices():
    url = "https://api.binance.com/api/v3/ticker/price"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        prices = {item["symbol"]: float(item["price"]) for item in data}
        usdt_prices = {}
        print(len(prices))
        for pair in prices:
            if "USDT" in pair:
                usdt_prices[pair] = prices[pair]

        print(len(usdt_prices))
        print(usdt_prices)

        return usdt_prices
    else:
        return {}  # Возвращаем пустой словарь в случае ошибки

def update_binance_pices():
    url = "https://api.binance.com/api/v3/ticker/price"
    response = requests.get(url)