from typing import Tuple, List
from decimal import Decimal

import requests

from cryptoportfolio.interfaces.base import Address


class NicehashWallet(Address):
    decimal_places = 18

    def __init__(self, id: str, key: str, **kwargs) -> None:
        self.id = id
        self.key = key
        super().__init__(**kwargs)

    def _get_addr_coins_and_tokens_balance(self) -> List[Tuple[str, Decimal]]:
        result = requests.get("https://api.nicehash.com/api?method=balance&id=%s&key=%s" % (self.id, self.key)).json()
        return [
            ("BTC", Decimal(result['result']['balance_confirmed']))
        ]
