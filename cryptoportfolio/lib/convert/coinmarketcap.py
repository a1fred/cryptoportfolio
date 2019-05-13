import requests
from decimal import Decimal

coins = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=0").json()


def get_price_usd(symbol):
    """
    :type symbol: str
    """

    print(f"GET for {symbol}")
    for token in coins:
        if token['symbol'] == symbol:
            return Decimal(token['price_usd'])
    return Decimal('0')
