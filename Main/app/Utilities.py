# Асинхронная функция для получения данных о криптовалютах
import aiohttp
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Dict


async def get_binance_coins(query: str) -> list:
    url = f"https://api.binance.com/api/v3/ticker/price"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    coins = []
                    # Перебираем монеты и проверяем, начинается ли символ монеты с введенного запроса
                    for coin in data:
                        symbol = coin["symbol"]
                        price = coin["price"]
                        if symbol.lower().startswith(query.lower()):
                            coins.append({
                                "symbol": symbol,
                                "price": price
                            })
                    return coins
                else:
                    return []
    except Exception as e:
        print(f"Ошибка при запросе: {e}")
        return []

