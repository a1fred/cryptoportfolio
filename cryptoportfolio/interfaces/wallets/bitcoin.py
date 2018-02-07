from decimal import Decimal
from typing import List, Tuple

import requests

from cryptoportfolio.interfaces.base import CryptoCoinWallet


class BitcoinWallet(CryptoCoinWallet):
    decimal_places = 18
    symbol = "BTC"

    def _get_addr_coin_balance(self) -> Decimal:
        balance_satoshi = requests.get(
            "https://blockchain.info/ru/balance?active=%s" % self.addr).json()[self.addr]['final_balance']
        return Decimal(balance_satoshi) / Decimal("100000000")

    def _get_addr_coin_tokens_balance(self) -> List[Tuple[str, Decimal]]:
        return []
