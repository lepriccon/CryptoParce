from telegram import InlineKeyboardMarkup, InlineKeyboardButton


class WrappedCoin:
    def __init__(self, symbol: str, price: float):
        self.symbol = symbol
        self.price = price
    def __str__(self):
        return f"{self.symbol} : {self.price}"

def get_inline_button(coin: WrappedCoin):
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("График SMA", callback_data=coin.symbol)]]
    )

def get_wrapped_coin(symbol: str, price: float):
    return WrappedCoin(symbol, price)