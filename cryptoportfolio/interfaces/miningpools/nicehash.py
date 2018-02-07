from typing import Tuple, List
from decimal import Decimal

import requests

from cryptoportfolio.interfaces.base import Address


class NicehashWallet(Address):
    decimal_places = 18
    symbol = "BTC"

    def __init__(self, id: str, key: str, **kwargs) -> None:
        self.id = id
        self.key = key
        super().__init__(**kwargs)

    def _get_addr_coin_tokens_balance(self) -> List[Tuple[str, Decimal]]:
        return []

    def _get_addr_coin_balance(self) -> Decimal:
        result = requests.get("https://api.nicehash.com/api?method=balance&id=%s&key=%s" % (self.id, self.key)).json()
        return Decimal(result['result']['balance_confirmed'])
