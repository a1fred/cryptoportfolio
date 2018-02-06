from typing import Tuple, List
from decimal import Decimal

import requests

from cryptoportfolio.wallets.abc import Wallet

NICEHASH_ADDRS = [
    # Id, key

]


class NicehashWallet(Wallet):
    decimal_places = 18
    symbol = "BTC"

    def __init__(self, name: str, credentials: Tuple[str, ...], percent_owned=Decimal('100'), decimal_places: int=None):
        self.credentials = credentials
        super().__init__(name=name, addrs=[name, ], percent_owned=percent_owned, decimal_places=decimal_places)

    def _get_addr_coin_tokens_balance(self, addr: str) -> List[Tuple[str, Decimal]]:
        return []

    def _get_addr_coin_balance(self, addr: str) -> Decimal:
        result = requests.get("https://api.nicehash.com/api?method=balance&id=%s&key=%s" % self.credentials).json()
        return Decimal(result['result']['balance_confirmed'])
