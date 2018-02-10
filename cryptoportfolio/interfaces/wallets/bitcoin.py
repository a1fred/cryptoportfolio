from decimal import Decimal
from typing import List, Tuple

import requests

from cryptoportfolio.interfaces.base import CryptoCoinWallet


class BitcoinWallet(CryptoCoinWallet):
    decimal_places = 18

    def _get_addr_coins_and_tokens_balance(self) -> List[Tuple[str, Decimal]]:
        balance_satoshi = requests.get(
            "https://blockchain.info/ru/balance?active=%s" % self.addr
        ).json()[self.addr]['final_balance']
        return [
            ("BTC", Decimal(balance_satoshi) / Decimal("100000000")),
        ]
