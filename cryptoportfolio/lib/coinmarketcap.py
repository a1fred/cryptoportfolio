from functools import lru_cache

import requests
from decimal import Decimal

coins = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=0").json()


@lru_cache(maxsize=512, typed=True)
def get_price_usd(symbol: str) -> Decimal:
    for token in coins:
        if token['symbol'] == symbol:
            return Decimal(token['price_usd'])
    return Decimal('0')
